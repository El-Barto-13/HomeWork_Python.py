#
# # HomeWork2
#
#
# Задача 10:
# print('На столе лежат n монеток.')
# print('Некоторые из них лежат вверх решкой, а некоторые – гербом. ')
# print('Определите минимальное число монеток, которые нужно перевернуть, ')
# print('чтобы все монетки были повернуты вверх одной и той же стороной. ')
# print('Выведите минимальное количество монет, которые нужно перевернуть.')
# *пример* 5 -> 1 0 1 1 0
#               2

# n = int(input("Введите количество монеток: "))
# orel = reshka = 0
# for i in range(n):
#     a = int(input("орел(1) или решка(0)"))
#     if a == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f' переверни {orel} монет с орла на решку их меньше всего')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')
# else:
#     print(f'переверни {reshka} монет с решки на орел их меньше всего')


# # Задача 12:
# print("Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. ")
# print("Он задумывает два натуральных числа X и Y (X,Y≤1000),")
# print("а Катя должна их отгадать. Для этого Петя делает две подсказки.")
# print("Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.")
# # *пример* 4 4 -> 2 2
# #          5 6 -> 2 3
#
# a = int(input("введите первое число которое задумал Петя: "))
# b = int(input("введите второе число которое задумал Петя: "))
#
# for i in range(a):
#     for j in range(b):
#         if a == i + j and b == i * j:
#             print(f'ето числа {i, j} отгадала Катя.')


# Задача 14:
# print("Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
# *пример* 10 -> 1 2 4 8
#
# N = int(input("Введи число: "))
# i = 0
# while 2 ** i <= N:
#     print(2 ** i)
#     i += 1
