# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.
# Ввод: Вывод:
# 1 2 3 2 3 2
import random

len1 = int(input("Размер список: "))
lst1 = [random.randint(0, 10) for _ in range(len1)]
print(lst1)
badlist = []
count=0
for i in range(len1):
    for j in range(i + 1, len1):
        if lst1[i] == lst1[j] and lst1[i] not in badlist:
            badlist.append(lst1[i])
            count+=1
print(count)


count = 0
for item in set(lst1):
    count += lst1.count(item)//2

print("===",count)