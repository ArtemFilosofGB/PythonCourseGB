На складе лежат разные фрукты в разном количестве.
# Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.

def total_fruits(**kwargs):
    summ=sum(kwargs.values())
    return summ

print(total_fruits(apples=10, bananas=5, oranges=8))