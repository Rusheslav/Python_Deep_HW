from fractions import Fraction

def get_lcm(x, y):
    if x > y:
        init_greater = x
    else:
        init_greater = y

    greater = init_greater

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += init_greater

    return lcm


def reduce_fraction(x, y):
    if x >= 0:
        a = x
    else:
        a = -x

    if y >= 0:
        b = y
    else:
        b = -y

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    gcd = a + b

    if x * y >= 0:
        return f"{int(x / gcd)}/{int(y / gcd)}".replace("-", "")
    elif x < 0:
        return f"-{int(-x / gcd)}/{int(y / gcd)}"
    else:
        return f"-{int(x / gcd)}/{int(-y / gcd)}"


fraction_one = input("Введите первую дробь: ")
fraction_two = input("Введите вторую дробь: ")

num_one, den_one = map(int, fraction_one.split("/"))
num_two, den_two = map(int, fraction_two.split("/"))

least_com_den = get_lcm(den_one, den_two)
new_num_one = int(least_com_den / den_one * num_one)
new_num_two = int(least_com_den / den_two * num_two)
new_com_num = new_num_one + new_num_two

mult_num = num_one * num_two
mult_den = den_one * den_two

fraction_sum = reduce_fraction(new_com_num, least_com_den)
fraction_mult = reduce_fraction(mult_num, mult_den)

print(f"Сумма дробей равна {fraction_sum}")
print(f"Сумма дробей равна {fraction_mult}")

a = Fraction(num_one, den_one)
b = Fraction(num_two, den_two)

print(str(a + b) == fraction_sum and str(a * b) == fraction_mult)
