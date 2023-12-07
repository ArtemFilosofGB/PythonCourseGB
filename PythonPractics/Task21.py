# Задача №21. Общее обсуждение
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

dict_list = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}
]


st = set()
for dct in dict_list:
    for values in dct.values():
        st.add(values)
print(*st)


#2 вариант с разделением
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": "S005", 4: 'new_key'}, {" V ":"S009"}, {" VIII":"S007 "}]
keys = set()
values = set()
for dct in data:
    for key, value in dct.items():
        keys.add(key)
        values.add(value)
print(keys)
print(values)