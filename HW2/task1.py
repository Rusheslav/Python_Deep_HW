def get_remainder(number):
    rem_dict = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f"
    }
    rem = number % 16
    return str(rem) if rem < 10 else rem_dict[rem]


num = int(input("Введите число: "))
if num < 0:
    x = -num
else:
    x = num

result = get_remainder(x % 16)
quotient = x // 16
while quotient != 0:
    result = get_remainder(quotient) + result
    quotient //= 16

if num < 0:
    result = "-" + result

print(result)
print(hex(num).replace("0x", "") == result)
