# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math

per_day = int(input("Сколько км  машина проезжает за день"))
total = int(input("Сколько пройдено всего км"))
#days = (per_day+total-0.000001)//per_day #//деление на цело
days = total//per_day+bool(total%per_day!= 0)
print(f'Понадобится {days} дн')

print(math.ceil(total / per_day))

days = (per_day+total)/per_day #//деление на цело
print(round(days)) # математическое округление
print(math.ceil(days)) # округление в большую сторону
print(math.floor(days))

# print(5+True)
# print(5+False)