# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

watermelon_cout = int(input("watermelon count: "))
max_weight = 0
min_weigth = 1000

for _ in range(watermelon_cout):
    watermelon = random.randint(1, 10)
    print(watermelon)
    if max_weight<watermelon:
        max_weight=watermelon
    if min_weigth>watermelon:
        min_weigth=watermelon
print(f"watermelon max weigth= {max_weight}")
print(f"watermelon min weigth= {min_weigth}")

max_ = float('inf')
min_ = float('-inf')

