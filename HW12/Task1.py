import csv


class Checker:
    param_dict = {'_name': ('Имя', 'имени'),
                  '_patronymic': ('Отчество', 'отчестве'),
                  '_surname': ('Фамилия', 'фамилии')}

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self,  value):
        if not value.istitle():
            raise ValueError(f'{self.param_dict[self.param_name][0]} необходимо писать с большой буквы.')
        if not value.isalpha():
            raise ValueError(f'В {self.param_dict[self.param_name][1]} все символы должны быть буквами')


class Range:
    param_dict = {'_marks': 'Оценки',
                  '_test_results': 'Результаты тестов'}

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        for item in value:
            self.validate(item)
        return setattr(instance, self.param_name, value)

    def validate(self,  value):
        if not self.start <= value <= self.end:
            raise ValueError(f'{self.param_dict[self.param_name]} должны быть в '
                             f'пределах от {self.start} до {self.end}. Неверное значение: {value}')


class Student:
    name = Checker()
    patronymic = Checker()
    surname = Checker()

    def __init__(self, name, patronymic, surname, file_name):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self._subjects = {}
        self.total_marks = 0
        self.count_marks = 0
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            for line in csv_reader:
                if line[0] == self.surname:
                    marks = [int(mark) for mark in line[2].split(',') if line[2]]
                    test_results = [int(result) for result in line[3].split(',') if line[3]]
                    subject = Subject(line[1], marks, test_results)
                    self._subjects[subject.name] = subject.marks, subject.get_avg_test_results()
                    self.total_marks += sum(subject.marks)
                    self.count_marks += len(subject.marks)

        self.avg_marks = self.total_marks / self.count_marks if self.count_marks else 'Оценок нет'


    def __str__(self):
        test_results = '\n'.join([f'{k}: {v[1]}' for k, v in self._subjects.items()])
        return f"{self.name} {self.patronymic} {self.surname}\n" \
               f"Средний балл по тестам:\n" \
               f"{test_results}\n" \
               f"Средняя оценка: {self.avg_marks}\n"


class Subject:
    marks = Range(2, 5)
    test_results = Range(0, 100)

    def __init__(self, name, marks, test_results):
        self.name = name
        self.marks = marks
        self.test_results = test_results

    def get_avg_test_results(self):
        return sum(self.test_results)/len(self.test_results) if self.test_results else 'Результатов нет'


student_one = Student('Семён', 'Евгеньевич', 'Авессалумов', 'students.csv')
student_two = Student('Павел', 'Вадимович', 'Вилков', 'students.csv')

print(student_one)
print(student_two)
