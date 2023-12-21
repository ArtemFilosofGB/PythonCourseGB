#lambda - анонимная фукция одна строка принимает и возвращает

# def func(x):
#     return x**2
#
# lambda x: x*2

x= "1234456789"
x= list(x)
print(x)
x=list(map(lambda x: int(x)*2,x))
print(x)

#map
a= "1234456789"
b=a
a=list(a)
print(a)
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

b=list(map(int,b))
print(b)

# filter отсеивает
print("filter")
for item in a:
    if item%2==0:
        b.append(item)
print(b)

b = list(filter(lambda x: x%2==0,a))
print(b)

# list comprihation
a = [int(x) for x in a if int(x)%2==0]
print(a)


#enumerate
a= "sadfsadfgdsa"

a=list(a)
print(a)
# for i in range(len(a)):
#     print(i,a[i])

for i, item in enumerate(a):
    print(i,item)

#zip
print("zip")
a= "sadfsadfg"
b="123456789"
a=list(a)
b=list(b)
c=[]
print(a,b)
for i in range(len(a)):
    c.append([a[i],b[i]])
t1=list(zip(a,b))
print(t1)
