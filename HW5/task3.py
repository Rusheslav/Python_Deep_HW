# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def get_fib():
    num_list = [0, 1]
    counter = -1
    while True:
        if counter < 1:
            counter += 1
            yield counter
        else:
            number = sum(num_list)
            num_list[0], num_list[1] = num_list[1], number
            yield number


fib_iter = get_fib()

print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
