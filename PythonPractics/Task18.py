# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.
#
# Пример:
#
#
list_1  = [1, 2, 5, 4, 11,0,-1]

# lst.sort()
print(list_1)
k = 6
print(list_1[min(range(len(list_1)), key=lambda i: abs(list_1[i] - k))])
# Код представляет собой поиск элемента из списка list_1, который наиболее близок к числу k.
#
# Первая строка кода создает список list_1 с элементами [1, 2, 5, 4, 11, 0, -1].
#
# Вторая строка кода определяет переменную k со значением 6.
#
# Третья строка кода выполняет следующие действия:
#
# Функция min() находит индекс элемента из списка list_1, который минимально отличается от числа k.
# Функция range(len(list_1)) создает последовательность чисел от 0 до количества элементов в списке list_1.
# Лямбда-функция lambda i: abs(list_1[i] - k) используется как ключ для сравнения элементов списка. Она вычисляет абсолютную разницу между текущим элементом списка и k.
# Функция min() возвращает значение элемента из списка list_1 с индексом, который получен из вызова функции min().
# Последнее выражение выводит найденный элемент из списка list_1, который наиболее близок к числу k.
# Итоговый результат будет зависеть от исходных данных в списке list_1 и числа k.


# # 5
#minimum = list_1[0]
# for i in range(len(list_1)):
#     print(list_1[i])
#     if k-list_1[i]>0:
#         minimum=k-list_1[i]
#     print(list_1[i]-k)

# def closest(lst, K):
#     return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# Driver code
#lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
# K = 6

# for i in range(len(list_1)):
#
#     if list_1[i]-k < minimum-k:
#         minimum = list_1[i]
#         print(abs(k - list_1[i]), "->", i, minimum)
#
# print(list_1, minimum)


# list_1 = [1, 2, 3, 4, 5,]
# k = 6
# for i in range(len(list_1)):
#     if list_1[i] < k:
#         nearest_num = -k
#     else:
#         nearest_num = nearest_num + 0
#         if list_1[i] >= k and list_1[i] - k <= nearest_num - k:
#             nearest_num = list_1[i]
#     elif list_1[i] <= k and nearest_num - k <= list_1[i] - k:
#         nearest_num = list_1[i]
# print(nearest_num)