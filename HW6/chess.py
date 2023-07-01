from random import randint


def check_position(pos: str) -> bool:
    queens = [int(q) for q in pos.split()]
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[j] // 10 == queens[i] // 10 or (queens[j] - queens[i]) % 10 == 0:  # проверка на один ряд или одну колонку
                return False
            if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 > queens[i] % 10) or
                (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 > queens[j] % 10)) and \
                    (queens[j] - queens[i]) % 11 == 0:  # проверка на диагональ "вправо-вниз"
                return False
            if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 < queens[i] % 10) or
                (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 < queens[j] % 10)) and \
                    (queens[j] - queens[i]) % 9 == 0:  # проверка на диагональ "влево-вниз"
                return False
    return True


def print_position(pos: str) -> None:
    queens = [int(q) for q in pos.split()]
    board = [[f'{i}'] + ['.'] * 8 for i in range(1, 9)]
    for queen in queens:
        board[queen // 10 - 1][queen % 10] = 'Q'
    print(' ', *[f'{i}' for i in range(1, 9)])
    for row in board:
        print(*row)


def random_position() -> str:
    pos = []
    while len(pos) < 8:
        queen = f'{randint(1, 8)}{randint(1, 8)}'
        if queen not in pos:
            pos.append(queen)
    return ' '.join(i for i in pos)


def get_all_positions() -> list[str]:
    results = []
    for cur_queen in range(11, 19):
        result = [str(cur_queen)]
        row = 2
        cell = 1
        while row < 9:
            while cell < 9:
                reviewed_queen = str(row * 10 + cell)
                tested_position = ' '.join(result) + ' ' + reviewed_queen
                if check_position(tested_position):
                    result.append(reviewed_queen)
                    if len(result) == 8:
                        results.append(' '.join(result))
                    if reviewed_queen[0] == '8' or len(result) == 8:
                        result.pop()
                        removed_queen = int(result.pop())
                        row = removed_queen // 10
                        cell = removed_queen % 10 + 1
                    else:
                        row += 1
                        cell = 1
                elif reviewed_queen[-1] == '8':
                    removed_queen = int(result.pop())
                    row = removed_queen // 10
                    cell = removed_queen % 10 + 1
                else:
                    cell += 1
                if not result:
                    break
            row += 1
            cell = 1
            if not result:
                break
    print(f'Все решений: {results}')
    print(f'Всего решений: {len(results)}')
    return results



