# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

from string import punctuation
print(punctuation)
#data = input("Enter your string: ").split()
data="She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
#data = data.lower().replace(".","").split()

for ch in punctuation:
    data=data.replace(ch," ")
data.lower().split()

print(data)


set_1= set()
for i in data:
    set_1.add(i)
print(set_1)
print(len(set_1))


