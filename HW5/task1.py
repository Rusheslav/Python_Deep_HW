# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_path(full_path):
    *path, name = full_path.split('/')
    return '/'.join(path) + '/', name, name.split('.')[-1]


example_path = '/Users/mike/Documents/Notes/tasks.md'

print(get_path(example_path))
