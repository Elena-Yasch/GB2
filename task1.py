# Задание 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['Kate', 1, 2.5, 3 < 4]
if type(my_list[0]) == str:
    print('OK')
else:
    print("NOK")
if type(my_list[1]) == int:
    print('OK')
else:
    print("NOK")
if type(my_list[2]) == float:
    print('OK')
else:
    print("NOK")
if type(my_list[3]) == str:
    print('OK')
else:
    print("NOK")
