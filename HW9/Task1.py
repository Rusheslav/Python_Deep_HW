from pathlib import Path
import csv
import json
import random


def deco_find_roots(func):
    def wrapper(*args, **kwargs):
        file_name = func()
        with open(file_name, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            numbers = [[int(num) for num in line] for line in csv_reader]
        for params in numbers:
            solve_equation(*params)
        return
    return wrapper


def deco_save_results(func):
    def wrapper(*args, **kwargs):
        my_file = Path('results.json')
        params = str(args)
        if my_file.is_file():
            with open('results.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                data[params] = func(*args, **kwargs)
            with open('results.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
        else:
            with open('results.json', 'w', encoding='utf-8') as json_file:
                json.dump({params: func(*args, **kwargs)}, json_file, ensure_ascii=False)
        return
    return wrapper


@deco_save_results
def solve_equation(a, b, c):
    if a == b == c == 0:
        return "Корней бесконечно много"
    if a == b == 0:
        return "Корней нет"
    if b == c == 0 or a == c == 0:
        return 0
    if a == 0:
        return - c / b
    discr = b ** b - 4 * a * c
    if discr > 0:
        return (- b + discr ** 0.5) / (2 * a), (- b - discr ** 0.5) / (2 * a)
    if discr == 0:
        return - b / (2 * a)
    if discr < 0:
        return "Корней нет"


@deco_find_roots
def generate_csv():
    number_of_lines = random.randint(101, 1001)
    numbers = [[random.randint(-100, 100) for _ in range(3)] for _ in range(number_of_lines)]
    file_name = "csv_numbers.csv"
    with open("csv_numbers.csv", 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in numbers:
            csv_writer.writerow(line)
    return file_name


generate_csv()
