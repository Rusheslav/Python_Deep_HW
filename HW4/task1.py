# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def remove_s():
    glob_dict = globals()
    for var in list(glob_dict):
        if len(var) > 1 and var[-1] == 's' and str(type(glob_dict[var])) != "<class 'function'>":
            glob_dict[var[:-1]] = glob_dict[var]
            glob_dict[var] = None

datas = [42, -37, 83, 45]
s = "Hello, world!"
names = "First Name", "Second Name", "Third Name"
sx = 42

print(datas)
print(s)
print(names)
print(sx)
print(globals())

remove_s()

print()
print(datas)
print(s)
print(names)
print(sx)
print(data)
print(name)
