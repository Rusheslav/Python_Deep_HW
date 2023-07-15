class Animal:
    alive = True

    def __init__(self, name: str, weight: int, height: int):
        self.name = name
        self.weight = weight
        self.height = height

    def get_name(self):
        return f'Имя животного: {self.name}'

    def get_weight(self):
        return f'Вес животного {self.name}: {self.weight} кг'

    def get_height(self):
        return f'Рост животного{self.name}: {self.height} см'

    def get_info(self):
        return f'Никакой дополнительной информации о животном {self.name} нет, поскольку класс животного не определен'


class Fish(Animal):
    habitat = 'вода'

    def __init__(self, name: str, weight: int, height: int, swimming_speed: int):
        self.swimming_speed = swimming_speed
        super().__init__(name, weight, height)

    def get_info(self):
        return f'Скорость плавания рыбы {self.name}: {self.swimming_speed} км/ч'


class Bird(Animal):
    habitat = 'воздух'

    def __init__(self, name: str, weight: int, height: int, wing_span: int):
        self.wing_span = wing_span
        super().__init__(name, weight, height)

    def get_info(self):
        return f'Размах крыльев птицы {self.name}: {self.wing_span} см'


class Wolf(Animal):
    habitat = 'земля'

    def __init__(self, name: str, weight: int, height: int, running_speed: int):
        self.running_speed = running_speed
        super().__init__(name, weight, height)

    def get_info(self):
        return f'Скорость бега волка {self.name}: {self.running_speed} км/ч'


class Factory:
    def get_animal(self, class_name: str, name: str, weight: int, height: int, special_parameter: int):
        classes = {
            'Fish': Fish,
            'Bird': Bird,
            'Wolf': Wolf
        }
        if class_name in classes:
            return classes[class_name](name, weight, height, special_parameter)
        else:
            print(f'Класса {class_name} нет. Создаем экземпляр класса Animal')
            return Animal(name, weight, height)


factory = Factory()
fish = factory.get_animal('Fish', 'Немо', 1, 5, 20)

print(fish.get_info())
