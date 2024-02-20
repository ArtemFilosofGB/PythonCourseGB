# Даны два списка: дата покупки dates, суммы покупок по датам income.
# Найти итоговую сумму всех покупок в ноябре и сохранить ее в переменную x.
# Используйте list comprehensions.

dates = ['2021-11-01']
income = [100]

# dates = ['2021-10-01', '2021-11-05', '2021-12-10']
# income = [100, 200, 300]

x = sum([income [i] for i in range (len(dates)) if dates[i].split('-')[1] == '11'])
#x = sum([x for x in income if dates[5:7] == '11'])
print(x)