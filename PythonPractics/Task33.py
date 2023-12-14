# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def change_journal(lst : list)-> list:
    maximum=0
    minimum=float('inf')
    for i in lst:
        if maximum<i:
            maximum=i
        if minimum>i:
            minimum=i
    print("max",maximum,"min",minimum)
    for i in range(len(lst)):
        if lst[i] == maximum:
            lst[i]=minimum
    return lst



journal = [-1, 3, 1616516165, 3, 4]


print(change_journal(journal))

