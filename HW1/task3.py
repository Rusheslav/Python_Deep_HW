# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

num = randint(0, 1000)
attempts = 10

while attempts > 0:
    number_str = input("Введите целое число от 0 до 1000: ")
    try:
        number = int(number_str)
        if number == num:
            print("Вы угадали!")
            break
        elif number < 0:
            print("Вы ввели отрицательное число.")
        elif number > 1000:
            print("Вы ввели число больше 1000")
        elif number < num:
            attempts -= 1
            print(f"Больше. Осталось попыток: {attempts} ")
        elif number > num:
            attempts -= 1
            print(f"Меньше. Осталось попыток: {attempts} ")

        if not attempts:
            print("У вас больше нет попыток. Вы проиграли!")

    except ValueError:
        print("Вы не ввели целое число.")