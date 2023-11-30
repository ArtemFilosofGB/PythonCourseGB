# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
import math
class1 = input("First class: ")
class2 = input("Second class: ")
class3 = input("Third class: ")

if not class1.isdigit() or not class2.isdigit() or not class3.isdigit():
    print("Enter a number!!!")
else:
    class1 = int(class1)
    class2 = int(class2)
    class3 = int(class3)
    result = (math.ceil(class1 / 2)) + ((class2 // 2) + class2 % 2) + ((class3 // 2) + class3 % 2)
    print(f"Desks: {result}")

    # Вариант решения 2

    result2 = (class1+1)/2+(class2+1)/2+(class3+1)/2
    print(f"Результат 2 : {result2}")