import json
from exceptions import *
from user import *


class Project:
    def __init__(self, users_list=None):
        if users_list is None:
            self.users_list = []
            self.ids_list = []
        else:
            self.users_list = users_list
            self.ids_list = [user.user_id for user in users_list]
        self.admin = None

    @classmethod
    def get_users_list(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            users_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in users_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        return cls(users_list)

    def login(self, name, user_id):
        user_to_check = User(name, user_id)
        if user_to_check not in self.users_list:
            raise AccessException(user_to_check.name, user_to_check.user_id)
        for user in self.users_list:
            if user == user_to_check:
                self.admin = user
                print(f'Пользователь {user_to_check} успешно зашел!')
                break

    def add_user(self, name, user_id, level):
        if self.admin is None:
            raise NoAdminException
        if level < self.admin.level:
            raise LevelException(level, self.admin.level)
        if user_id in self.ids_list:
            raise DoubleIdException(user_id)
        self.users_list.append(User(name, user_id, level))
        self.ids_list.append(user_id)

    def del_user(self, name, user_id, level):
        if level < self.admin.level:
            raise LevelException
        try:
            self.users_list.remove(User(name, user_id, level))
        except ValueError:
            print('Пользователя нет в списке!')

    def save_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            users_dict = {}
            for user in self.users_list:
                if user.level not in users_dict:
                    users_dict[user.level] = {user.user_id: user.name}
                else:
                    users_dict[user.level][user.user_id] = user.name
            json.dump(users_dict, file, ensure_ascii=False)


p = Project().get_users_list('users.json')
print(p.users_list)
p.login('ben', 1)
print(p.admin)
p.add_user('andy', 4, 3)
p.save_file('users_test.json')

p.add_user('sergey', 4, 2)

# p = Project([User('andy', 1, 2)])
# p.login('andy', 1)
# p.add_user('ben', 2, 1)
# print(p.users_list)
