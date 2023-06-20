# def get_remainder(number):
#     rem_dict = {
#         10: "a",
#         11: "b",
#         12: "c",
#         13: "d",
#         14: "e",
#         15: "f"
#     }
#     rem = number % 16
#     return str(rem) if rem < 10 else rem_dict[rem]
hex_list = '0123456789abcdef'

num = int(input("Введите число: "))
if num < 0:
    x = -num
else:
    x = num

result = hex_list[x % 16]
quotient = x // 16
while quotient != 0:
    result = hex_list[quotient % 16] + result
    quotient //= 16

if num < 0:
    result = "-" + result

print(result)
print(hex(num).replace("0x", "") == result)
