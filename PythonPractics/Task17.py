# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
list_1 = list_2= [1, 1, 2, 0, -1, 3, 4, 4]
list_1 = set(list_1)
print(len(list_1))

list_3=[]
for i in list_2:
    if i not in list_3:
        list_3.append(i)
print(len(list_3))