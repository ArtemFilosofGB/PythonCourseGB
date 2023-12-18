import random

lst = [[1,2],[3,4]]
print([max(i) for i in lst]) # [2, 4]

# list comprehension
# dict comprehension
# cortege comprehension
# tuple comprehension do bot work  !!! generator !!!


obj1=[random.randint(0,100) for _ in range(10)]
obj2={random.randint(0,100): random.randint(-10,0) for _ in range(10)}
obj3={random.randint(0,100) for _ in range(10)}
obj4=(random.randint(0,100) for _ in range(10))

print(obj1)
print(type(obj1))
print(obj2)
print(type(obj2))
print(obj3)
print(type(obj3))
print(obj4)
print(type(obj4))