import logging
from users.models import CustomUsers

logger = logging.getLogger(__name__)


def add_object(request, obj):
    user = get_user_info(request)
    logger.info(f"User {user} add object {obj}.")
# Логирование удаления объекта
def delete_object(request, obj):
    user = get_user_info(request)
    logger.info(f"User {user} deleted object {obj}.")

# Логирование изменения объекта
def edit_object(request, obj):
    user = get_user_info(request)
    logger.info(f"User {user} edited object {obj}.")

# Логирование входа в систему
def user_logged_in(request):
    user = get_user_info(request)
    logger.info(f"User {user} logged in.")

# Логирование выхода из системы
def user_logged_out(request):
    user = get_user_info(request)
    logger.info(f"User {user} logged out.")

# Вспомогательная функция для получения информации о пользователе
def get_user_info(request):
    user = None
    if request.user.is_authenticated:
        user = CustomUsers.objects.get(username=request.user)
    else:
        user = "Anonymous"
    return user
