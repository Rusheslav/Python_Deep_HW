class MainException(Exception):
    pass


class LevelException(MainException):
    def __init__(self, level, admin_level):
        self.level = level
        self.admin_level = admin_level

    def __str__(self):
        return f'Ошибка уровня доступа! Ваш уровень - {self.admin_level}. Вы пытаетесь создать пользователя ' \
               f'с уровнем {self.level}'


class AccessException(MainException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'У пользователя {self.name}, id = {self.user_id} нет прав доступа!'


class NoAdminException(MainException):
    def __str__(self):
        return 'В проекте нет админа! Сначала создайте админа!'


class DoubleIdException(MainException):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'Пользователь с id = {self.user_id} уже существует!'
