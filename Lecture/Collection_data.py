#Коллекция
list_1 =[] # список
tuple_1 =() #кортеж (неизменяемый тип) a=(1,) - кортеж
set_1 = {} #множества содержит неизменяемые типы данных
dict_1 ={} #словарь ключ : значение ключ-неизметяемый тип данных(id - eуникальный)



dct = {"один":1,2:"Два"}
print(dct)
print(dct[2])

print("\n")
print(dct["один"])
print(dct.get("два",2))

dct[4] = "четыре"
print(dct)

dct.pop(4) # удаление по ключу 4

dct[5] = "пять"
print(dct)
for key in dct:
    print(dct.get(key))


my_set = {1,2,3,4}
my_set = {1:"one",2:"two",3:"thee",4:"four"}