# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
from random import uniform, randint
from math import pi


def find_farthest_orbit(a, b):
    return pi * a * b


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# orbits = [(round(uniform(1,15),2),uniform(1,15)) for _ in range(5)] # float random
orbits = [(randint(1, 5), randint(1, 5)) for _ in range(5)]
print(orbits)
print(orbits:= set(filter(lambda x: x[0] != x[1], orbits)))
print(sorted(orbits,key=lambda x: x[0]*x[1],reverse=True))


# for i in
#
# result= list(map(find_farthest_orbit(a),orbits))
#
#
# print(*find_farthest_orbit(orbits))
