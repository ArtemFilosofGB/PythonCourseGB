# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
#
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
#
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
import array


# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     for i in range(1, num_rows + 1):
#         print(i, end=' ')
#         for j in range(1, num_columns + 1):
#             print(j, end=' ')
#             print(operation(i, j), end=' ')
#         print()

#функция эталонного решения
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            row = [str(i)]
            for j in range(2, num_columns + 1):
                row.append(f'{operation(i, j)}')
            print(' '.join(row))




print_operation_table(lambda x, y: x * y, 3, 3)
print("++++++++++++")
print_operation_table(lambda x, y: x + y, 4, 4)
print("++++++++++++")
print_operation_table(lambda x, y: x - y, 5, 5)
print("++++++++++++")
print_operation_table(lambda x, y: x * y, 1, 2)
print("++++++++++++")
print_operation_table(lambda x, y: x / y, 4, 4)
print("++++++++++++")
print_operation_table(lambda x, y: x * y)


