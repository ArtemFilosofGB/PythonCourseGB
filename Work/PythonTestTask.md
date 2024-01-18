## Python Test Tasks

```
def get(n, a):
    print(f'My name is {n} and my age is {a/10:.5f}')
get('Lej',31)


# My name is Lej and my age is 3.10000
```

```
n=enumerate("John")
for i,j in n:
    print(i,j,end=",sep=")

#0 J,sep=1 o,sep=2 h,sep=3 n,sep=
```
```
name ='Jon'
print('Hi',%d'%name)

#error
```
```
x=23
n=0 if x>10 else 11
print(n)

# 0
```
```
print(False == False in [False])
print((False==False) and (False in[False]))

#True True
```
```
a=([],)
a[0].extend([1])
print(a[0]==[1])

#True
```
```
import random
x=[1,2,3]
print(x)
random.shuffle(x)
print(x)

#перемешивает значения списка
```

```
import random
x=[1,2,3]
print(x)
random.shuffle(x)
print(x)

#NUMPY нет в стандартных модулях
```
```
#mutable type в python List Dictionary Set
```

```
def f(a,*pargs,**kargs):
    print(a)
    print(pargs)
    print(kargs)

f(1,2,3,x=4,y=5)

#1 (2, 3) {'x': 4, 'y': 5}
```
```
for i in range(5):
    if i%2 == 0:
        continue
    print(i)

# 1 3
```
```
a,*b,c = [1,2]
print(a,b,c)

#1 [] 2
```