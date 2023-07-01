from chess import *
from random import randint

position = '11 25 38 46 53 67 72 84'

if __name__ == "__main__":
    all_positions = get_all_positions()
    print('Вывод случайной позиции из списка результатов:')
    print_position(all_positions[randint(0, len(all_positions) - 1)])

    print("\nИщем 4 решения рандомом (но вряд ли найдём):")
    result = []
    while len(result) < 4:
        pos = random_position()
        if check_position(pos):
            result.append(pos)
            print(f'Найдено позиций: {len(result)} -> {result}')
    for i in result:
        print_position(i)
