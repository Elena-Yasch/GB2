#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []

for i in range(5):
    number = int(input("Введите число: "))
    my_list.append(number)

print(my_list)

# my_list = ["a", "b", "c"]
for index, value in enumerate(my_list):
    if index % 2 == 1:
        tmp = my_list[index - 1]
        my_list[index - 1] = my_list[index]
        my_list[index] = tmp

print(my_list)






