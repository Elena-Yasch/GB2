# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running  (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

# import time
#
#
# class TrafficLight:
#     __trafficlight_color = 'Красный'
#
#     def running(self):
#         self._trafficlight_color = 'Желтый'
#         print('Сигнал светофора: "Желтый"')
#         time.sleep(2)
#         self._trafficlight_color = 'Зеленый'
#         print('Сигнал светофора: "Зеленый"')
#         time.sleep(7)
#         self._trafficlight_color = 'Красный'
#         print('Сигнал светофора: "Красный"')
#         time.sleep(7)
#
#
# tl1 = TrafficLight()
# while True:
#     tl1.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 0.05м = 125т

# class Road:
#     _road_length = 5000
#     _road_width = 20
#
#     def calk_road_mass(self, mass_road, depth):
#         print(self._road_length * self._road_width * mass_road * depth)
#
# road1 = Road()
# road1.calk_road_mass(25, 0.05)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров).
#
# class Worker:
#     name = ''
#     surname = ''
#     position = ''
#     _income = ''
#
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, income):
#         super().__init__(name, surname, position, income)
#
#     def get_full_name(self):
#         print(self.name, self.surname)
#
#     def get_total_income(self):
#         print(self._income["wage"] + self._income['bonus'])
#
#
# posi1 = Position("Elena", "Yaschehko", "QA", {"wage": 120000, "bonus": 60000})
# posi1.get_full_name()
# posi1.get_total_income()
# posi2 = Position ("Swyatoslav", "Yaschenko", "QA", {"wage": 420000, "bonus": 100002})
# posi2.get_full_name()
# posi2.get_total_income()

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = ''
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Скорость машины:', self.speed)

    def pol_car(self):
        if self.is_police:
            print('Это полицейская машина!')
        else:
            print('Это машина горожанина.')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)
        if self.speed > 60:
            print('Внимание! Превышение скорости!')


t_car = TownCar(75, 'Синяя', 'KIA')
t_car.show_speed()
t_car.pol_car()


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)


s_car = SportCar(155, 'Красный', 'Porsche 911 GT3')
s_car.show_speed()
s_car.pol_car()


class WorkCar(Car):
    model = 'ГАЗель'

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)
        if self.speed > 40:
            print('Внимание! Превышение скорости!')



w_car = WorkCar(35, 'Серебряная', 'ГАЗель')
w_car.show_speed()
w_car.pol_car()


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


p_car = PoliceCar(60, 'Белая', 'PoliceCar')
p_car.show_speed()
p_car.pol_car()
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.
#
# class Stationery:
#     title = ''
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(self.title, 'Запуск отрисовки.')
#
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         print(self.title, 'Чертеж ручкой.')
#
#
# class Pensil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         print(self.title, 'Чертеж карандашом.')
#
#
# class Handle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         print(self.title, 'Выделение маркером.')
#
#
# some_stat1 = Pen("Ручка -")
# some_stat1.draw()
# some_stat2 = Pensil("Карандаш -")
# some_stat2.draw()
# some_stat3 = Handle("Маркер -")
# some_stat3.draw()
