# Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(),
# которая на вход принимает список с датами и список с выручкой, а на выходе словарь,
# где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.



dates = ['2021-10-01', '2021-11-05', '2021-12-10']
income = [100, 200, 300]

def calc_income_by_month(dates, incomes):
    income_by_month = {}

    for i in range(len(dates)):
        month = dates[i].split('-')[1]
        if month in income_by_month:
            income_by_month[month] += incomes[i]
        else:
            income_by_month[month] = incomes[i]

    return income_by_month

print(calc_income_by_month(dates, income))