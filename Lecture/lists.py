list_1 =[1,2,2.2]

print(*list_1)
print("Вывод элементов списка")
for i in list_1:
    print(i)

print(len(list_1))

print(list_1[2])

print("добавляет значение к списку")
list_1=[1,5]
print(list_1)
list_1.append(8) #добавляет значение к списку
print(list_1)

for i in range(5):
    list_1.append(i)
    print(list_1)
print("Удаляет элемент списка и возвращает индекс")
for j in range(5):
    index = list_1.pop() # Удаляет элемент списка и возвращает индекс
    print(list_1)
    print(index)
print("удаление элемента с индексом 1")
print(list_1)
list_1.pop(1) #удаление элемента с индексом 1
print(list_1)

print("Добавление элемента списка")
print(list_1)
list_1.insert(1, 1111)
print(list_1)

list_2 = [1,2,3,4,5,6,7,8,9]
list_1.append(list_2)
print(list_1)

# Срезы

print(list_2[0])
print(list_2[1])
print(list_2[-1])
print(list_2[:])
print(list_2[2:4]) # от индекса 2 до 4 (не включая последний)
print(list_2[1:8:2])# почему последний выводит?
print(list_2[::2])#

