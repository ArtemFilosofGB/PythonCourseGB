def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

calc3 = lambda a, b: a + b

math(calc1, 5, 2)  # 7
math(calc2, 5, 2)  # 10
math(calc3, 5, 2)  # 7
math(lambda a, b: a + b,5,2) #7
