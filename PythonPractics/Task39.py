# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

len1 = int(input("Размер 1 массива: "))
len2 = int(input("Размер 2 массива: "))


lst1=[random.randint(0,10) for _ in range(len1)]
lst2=[random.randint(0,10) for _ in  range(len2)]

set1=set(lst2) #Второй список переводим во множество тк не важен порядок второго списка

print(lst1)
print(lst2)


# # Второй
# for elem in lst1:
#     if elem not in set1:
#         print(elem," " ,end ="")
#
#
# import random
# n = int(input('Список первый задай: '))
# n2 = int(input('Список второй задай: '))
# list1 = [random.randint(1,15) for _ in range(n)]
# list2 = [random.randint(1,15) for _ in range(n2)]
# print(list1)
# print(list2)
#
# change = set(list1) - set(list2)
#
# for i in list1:
#     if i in change:
#         print(i, end= ' ')