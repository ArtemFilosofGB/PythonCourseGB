# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# Натуральное число больше 1, у которого есть всего два делителя: единица и само число. Например: 11, 13, 17, 19 — список простых чисел.

def prime_number(number):
    # отработка исключений
    if number in (1, 2):
        return True
    # проверка на чётность
    if not number % 2:
        return False

    for i in range(3, int(number ** 0.5), 2):  # number**0.5 квадратный корень числа
        if not number % i:
            return False
    return True


def is_prime(number):
    if number in range(3):
        return True
    if not number % 2:
        return False

    for i in range(3, int(number ** 0.5), 2):  # number**0.5 квадратный корень числа
        if number % i == 0:
            return False
    return True


#
# #print(prime_number(int(input("Enter a number: "))))


print(prime_number(17))

print(is_prime(17))
