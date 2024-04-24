from django.db import models
from django.db.models import Max

class SixDigitAutoField(models.AutoField):
    def pre_save(self, model_instance, add):
        if add:
            # Получаем максимальное значение поля 'invent'
            max_value = model_instance.__class__.objects.aggregate(Max('invent'))['invent__max'] or 99999
            # Генерируем новое шестизначное значение
            value = max_value + 1
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)


class Edinica(models.Model):
    title = models.ForeignKey('Tehnika', verbose_name='Вид техники', max_length=256, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    seriniy = models.CharField('Сериный номер', max_length=256)
    invent = SixDigitAutoField('Номер инвентаризации', primary_key=True)
    sklad = models.ForeignKey('Sklads', verbose_name='Склад', max_length=50, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    etazh = models.ForeignKey('Etazh', verbose_name='Этаж', max_length=50, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    kabinet = models.ForeignKey('Kabinet', verbose_name='Кабинет', max_length=50, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    brand = models.CharField('Производитель', max_length=256)
    modelmodel = models.CharField('Модель', max_length=256)
    remont = models.BooleanField('В ремонте', default=False, null=True)
    lico = models.CharField('Ответственный', max_length=256, null=True, blank=True, default=None)
    mac = models.CharField('MAC-адрес', max_length=256, null=True, blank=True, default=None)

    def __str__(self):
        return self.seriniy

    class Meta:
        verbose_name = 'Единица'
        verbose_name_plural = 'Единицы'


class Tehnika(models.Model):
    title = models.CharField('Вид техники', max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид техники'
        verbose_name_plural = 'Вид техники'

class Kabinet(models.Model):
    title = models.CharField('Номер кабинета', max_length=100)
    etazh = models.ForeignKey('Etazh', verbose_name='Этаж', max_length=50, null=True, blank=True, default=None, on_delete=models.SET_NULL)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

class Etazh(models.Model):
    title = models.CharField('Этаж', max_length=50)
    sklad = models.ForeignKey('Sklads', verbose_name='Склад', max_length=50, null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'


class Sklads(models.Model):
    title = models.CharField('Адрес', max_length=50)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    
