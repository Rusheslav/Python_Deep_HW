# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from itertools import permutations

things = {'свитер': 1, 'книга': 2, 'ложка': 1, 'консерва': 3, 'ноутбук': 5, 'свирель': 1, 'шлёпанцы': 2, 'гитара': 7}
max_weight = int(input("Введите максимальный вес: "))

result = []

total_weight = 0
for thing in things.keys():
    total_weight += things[thing]
if total_weight <= max_weight:
    result.append(set(things.keys()))

for permutation in permutations(things):
    perm_lst = list(permutation)
    weight = total_weight
    while weight > 0:
        weight -= things[perm_lst.pop()]
        set_things = set(perm_lst)
        if 0 < weight <= max_weight and set_things not in result:
            result.append(set_things)

for cur_set in result:
    cur_weight = 0
    for i in cur_set:
        cur_weight += things[i]
    print(cur_set, cur_weight)
