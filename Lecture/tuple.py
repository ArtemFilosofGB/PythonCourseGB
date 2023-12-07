t = ()  # кортеж
print(type(t))
t = (1)
print(type(t))
t = (1, 2, 3.1)
print(type(t))

v = [5, 6, 7]  # список
print(v)
print(type(v))

v = tuple(v)  # кортеж
print(v)
print(type(v))

a, b = 1, 2  # a==1 b==2

a, b, c = v

print(a, b, c)

# output tuple
t = (1, 2, 3.1, 4, 56)

for i in t:
    print(i)

for i in range(len(t)):
    print(f"{i}->{t[i]}")
