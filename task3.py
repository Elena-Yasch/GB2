#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input("Введите номер месяца:"))
# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
# if month in winter:
#     print("На дворе Зима")
# if month in spring:
#     print("На дворе Весна")
# if month in summer:
#     print("На дворе Лето")
# elif month in autumn:
#     print("На дворе Осень")

my_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8],"Осень": [9, 10, 11]}
for season, months in my_dict.items():
    if month in months:
        print(season)
        break