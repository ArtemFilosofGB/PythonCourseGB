# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу:
#
# “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”.
#
# Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Ваня:
# n = int(input())
# max_number = 0 #2
# while n != 0:
#     if max_number < n:#3
#         max_number = n
#     n = int(input()) #1
# print(max_number)
# #Петя:
n = int(input())
max_number = float('-inf')
while n > 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)

# function print max number of list
def max_num(x):
    max = x[0]
    for i in x:
        if max < i:
            max = i
    return max

# function prints hello world
def hello_world():
    print("Hello World!")