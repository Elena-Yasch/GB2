#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user = input("Введите строку:")
my_list = user.split()
for index, element in enumerate(my_list):
    print(index, element[:10])