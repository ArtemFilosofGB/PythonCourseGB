# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
list_1 = [11, 22, 33, 44, 55]
# key = input("Введите")
key = 22
list_2 = []
key = key % len(list_1)+1
for i in range(len(list_1)):
    if (i + key) > len(list_1) - 1:
        temp = i + key - len(list_1)
        list_2.append(list_1[temp])
    else:
        list_2.append(list_1[i + key])
print(list_2)

#Второй вариант
# my_list = [1, 2, 3, 4, 5,6,7,8,9]
# k = 3
# shifted_list = my_list[k:] + my_list[:k]
#
# print(shifted_list)

# ТРЕТИЙ ВАРИАНТ ЧЕРЕЗ ИНДЕКСЫ
# lst = [111, 222, 333, 444, 555]
#
# lst_shifted = []
# shift = 3
# for i in range(len(lst)):
#     lst_shifted.append(lst[(i + shift) % len(lst)])
# print(lst_shifted)