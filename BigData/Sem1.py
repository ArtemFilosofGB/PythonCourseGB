#Ваше решение


def my_square(num):
    result = []
    for i in num:
        result+=i*i
    return num


numbers = [1, 2, 3, 4, 5]

result = list(map(my_square,numbers))
print(result)

