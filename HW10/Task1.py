from inspect import signature


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
    def __init__(self, _class, *args):
        self._class = _class
        self.params = args

    def get_animal(self):
        classes = [Fish, Bird, Wolf]
        if self._class in classes and len(self.params) == 4:
            return self._class(*self.params)
        elif self._class not in classes:
            print(f'Класса {self._class} нет.')
            return None
        else:
            print(f'Параметров передано: {len(self.params)}. Для класса {self._class.__name__} '
                  f'необходимо {len(signature(self._class.__init__).parameters) - 1}.')
            return None


factory = Factory(Fish, 'Немо', 1, 5, 20)
fish = factory.get_animal()

print(fish)
