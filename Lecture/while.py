i=0
while i<5:
    print(i)
    i+=1
else:
    print("Конец программмы")
print(i+10)

n = int(input("Введите число для поиска минимального делителя"))
flag = True
i=2
while flag:
    if n%i ==0:
        flag = False
        print(i)
    elif i>n//2:
        print(n)
        flag=False
    i+=1