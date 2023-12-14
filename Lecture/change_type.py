a=[1,2,3]
b=a
print(a)
print(b)

a.append(4)
print(a)
print(b)

b=a.copy()
a.append(5)
print(a)
print(b)

# a[4].append(6)
# print(a)
# print(b)

a = []
for _ in range(5):
    a.append(input(f"Введите :"))

a=input("введите строку с пробелом").split()

for i in range(len(a)):
    a[i] = int(a[i])
print(a)
print(type(a))
for i in range(100):
    print()
    if i=10:
        if i=20:

