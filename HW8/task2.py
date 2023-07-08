# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle


def read_csv(path):
    with open(path, 'r') as file:
        data = list(csv.reader(file))
    headers = data.pop(0)
    result = []
    for row in data:
        dct = {}
        for i, cell in enumerate(row):
            dct[headers[i]] = cell
        result.append(dct)
    pickle_result = pickle.dumps(result)
    print(pickle_result)


read_csv("/Users/andrejlebedev/Documents/Geekbrains/Python_Deep_HomeWork/HW8/result.csv")
