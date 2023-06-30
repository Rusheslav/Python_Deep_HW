# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Антон", "Бограт", "Владимир"]
salaries = [50000, 100000, 150000]
bonuses = ["5.00", "7.25", "10.25"]

bonuses_dict = {name: salary * float(bonus) / 100 for name, salary, bonus in zip(names, salaries, bonuses)}

print(bonuses_dict)
