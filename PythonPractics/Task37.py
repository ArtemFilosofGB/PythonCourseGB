# Задача №37. Общее обсуждение
# 5 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_number(n):
    return int(str(n)[::-1])


print(reverse_number(12345))


def reverse_number_2(n):
    if n > 0:
        # return n%10*10**(len(str(n))-1) + reverse_number_2(n//10)
        return int(str(n % 10) + str(reverse_number_2(n // 10)))
    else:
        return 0


print(reverse_number_2(12345))


#вариант с ручным вводом и рекурсией
def reverse_number_3(number):
    if number==0:
        return ''
    s=input("Введите что-то: ")
    return reverse_number_3(number-1)+s


print(reverse_number_3(5))