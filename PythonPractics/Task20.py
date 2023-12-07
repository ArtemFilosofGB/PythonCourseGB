# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# Пример:
#
#
k = 'ноутбук'
# 12

list_en1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]  # – 1 очко;
list_en2 = ["D", "G"] # – 2 очка;
list_en3 = ['B', 'C', 'M', 'P']  # – 3 очка;
list_en4 = ['F', 'H', 'V', 'W', 'Y']  # – 4 очка;
list_en5 = ['K']  # – 5 очков;
list_en8 = ['J', 'X']  # – 8 очков;
list_en10 = ['Q', 'Z']  # – 10 очков.

list_ru1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']  # – 1 очко;
list_ru2 = ['Д', 'К', 'Л', 'М', 'П', 'У']  # – 2 очка;
list_ru3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']  # – 3 очка;
list_ru4 = ['Й', 'Ы']  # – 4 очка;
list_ru5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']  # – 5 очков;
list_ru8 = ['Ш', 'Э', 'Ю']  # – 8 очков;
list_ru10 = ['Ф', 'Щ', 'Ъ']  # – 10 очков.
count=0
#print(type(k))
key_list=list(k.upper())
#print(key_list)
for i in key_list:
    if i in list_ru1:count+=1
    elif i in list_ru2: count += 2
    elif i in list_ru3:count += 3
    elif i in list_ru4:count += 4
    elif i in list_ru5:count += 5
    elif i in list_ru8:count += 8
    elif i in list_ru10:count += 10
    if i in list_en1:count+=1
    elif i in list_en2: count += 2
    elif i in list_en3:count += 3
    elif i in list_en4:count += 4
    elif i in list_en5:count += 5
    elif i in list_en8:count += 8
    elif i in list_en10:count += 10

print(count)

