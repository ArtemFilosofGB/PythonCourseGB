# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

lst = [1, 2, 3, 5, 8, 15, 23, 38]

def sqrt(a):
    return a*a


# lst_res=[]
# for i in lst:
#     if i%2==0:
#         lst_res.append((i,sqrt(i)))
#
# print(lst_res)


#variant2
# def where(f,col):
#     return [x for x in col if f(x)]
#
# res = map(int, lst)
# print(res)
# res = where(lambda x: x%2==0, res)
# print(res)
# res = list(map(lambda x: (x, sqrt(x)), res))
# print(res)

#variant3


res = map(int, lst)
print(res) #выводит адрес map
res = filter(lambda x: x % 2 == 0, res)
print(res) #выводит адрес filter
res = list(map(lambda x: (x, sqrt(x)), res))
print(res)