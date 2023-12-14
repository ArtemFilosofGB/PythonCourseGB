# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.
#
# Пример:
#
#
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# Введите ваше решение ниже

def f(a:int,b:int):
    if b==1:
        return a
    return a*f(a,b-1)

a = 3
b = 5
print(f(a, b))


