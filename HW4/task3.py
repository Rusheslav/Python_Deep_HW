# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#

def get_dict(first=None, second=None, third=None):
    result = {}
    for k, v in locals().items():
        if v and v.__hash__:
            result[v] = k
    return result


print(get_dict(first=1, second=[2, 3], third='abc'))
