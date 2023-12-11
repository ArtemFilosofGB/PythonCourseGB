text = ('She sells sea shells on the sea shore The shells that she '
        'sells are sea shells I\'m sure. So if she sells sea shells on '
        'the sea shore I\'m sure that the shells are sea shore shells')
lst_text = text.lower().split()
print(lst_text)
lst = set(lst_text)
for word in lst_text:
    if word not in lst_text:
        lst.add(word)
print(len(lst))


Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)
Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)