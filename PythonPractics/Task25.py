# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# str="a a a b c a a d c d d"
#
# lst=[]
# lst= str.split()
# print(lst)
# res=[]
# count=0
#
# for i in lst:
#
#     for j in lst:
#         count+=1
#     res.append(lst[i]+"_"+str(count))
#     count=0
#
# print(res)

# string = input("Enter your string: ").split()
# instances = {}

# for item in string:
#     print(instances)
#     if item not in instances:
#         instances[item] = 1
#         print(f"{item}", end=" ")
#     else:
#         print(f"{item}_{instances[item]}", end=" ")
#         instances[item] += 1
#
# print(string)
# print(instances)
i=1
data = input("Enter your string: ").split()
dict_counter = {}

for char in data:
    print(f"{i}-й шаг",dict_counter)
    i+=1
    #qprint(f'{char}_{dict_counter.get(char)}', end=" ") if char in dict_counter else print(char,end=" ") # тернарный оператор
    dict_counter[char] = dict_counter.get(char,0)+1
print(dict_counter)
