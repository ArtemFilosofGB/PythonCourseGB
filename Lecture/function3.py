import module_sum as ms

#print(ms.max1(5,10))
print("Фибоначи")
print(ms.fibonachi(5))

list_1 =[]
for i in range(1,10):
    list_1.append(ms.fibonachi(i))
print(list_1)