from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def get_by_natural_key(self, username):
        return self.get(username=username)
    
    
class CustomUsers(AbstractBaseUser):
    username = models.CharField('Логин', max_length=50, unique=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    is_staff = models.BooleanField('Администратор', default=False)
    is_superuser = models.BooleanField('Суперпользователь', default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    
    def has_perm(self, perm, obj=None):
        # Ваша реализация проверки прав доступа
        return True

    def has_module_perms(self, app_label):
        # Ваша реализация проверки прав доступа к модулю
        return self.is_staff
