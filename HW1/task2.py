# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

bad_input = True

while bad_input:
    number_str = input("Введите целое число от 0 до 100 000: ")
    try:
        number = int(number_str)
        if 0 <= number <= 100000:
            bad_input = False
        elif number < 0:
            print("Вы ввели отрицательное число.")
        else:
            print("Вы ввели число больше 100 000")
    except ValueError:
        print("Вы не ввели целое число.")

if number in (0, 1):
    print(f"Число {number} не является ни простым, ни составным.")

else:
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            print(f"Число {number} составное.")
            break

    else:
        print(f"Число {number} простое.")
