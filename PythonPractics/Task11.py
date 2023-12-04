# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Элементы числовой последовательности

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, … (последовательность A000045 в OEIS)

# n = int(input("Enter n fibonumber: "))
# fib_number, fib_number1 = 0, 1
# counter = 2
# while fib_number + fib_number < n:
#     fib_number, fib_number1 = fib_number1, fib_number + fib_number1  # замена значений переменных
#     print(fib_number)
#     counter += 1
# if n == 0:
#     print(1)
# elif n == 1:
#     print("Couter plase 2 or 3")
# elif (fib_number + fib_number1 == n):
#     print(counter + 1)
# else:
#     print(-1)


number_a = int(input("Enter a number: "))

fib_number, fib_number1 = 0, 1
counter = 2

while fib_number + fib_number1 < number_a:
    fib_number, fib_number1 = fib_number1, fib_number + fib_number1
    counter += 1

if number_a == 0:
    print(1)
elif number_a == 1:
    print("Fibonachi position: 2 or 3")
elif fib_number + fib_number1 == number_a:
    print(f"Fibonachi position: {counter + 1}")
else:
    print(-1)