# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle
from pathlib import Path


def pickle_to_csv(path):
    with (open(path, 'rb') as pickle_file,
          open(str(Path(path).parent.absolute()) + '/result.csv', 'w') as csv_file):
        data = pickle.load(pickle_file)
        headers = []
        for dct in data:
            for header in dct.keys():
                if header not in headers:
                    headers.append(header)
        csv_write = csv.DictWriter(csv_file, fieldnames=headers)
        csv_write.writeheader()
        for dct in data:
            csv_write.writerow(dct)


pickle_to_csv("/Users/andrejlebedev/Documents/Geekbrains/Python_Deep_HomeWork/HW8/pickle_table.pickle")
