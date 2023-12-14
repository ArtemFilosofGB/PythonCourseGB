user = ["user1", "user2", "user3", "user4", "user5"]

ids = [4, 5, 9, 14, 7]
lst=list(zip(ids,user))
print("list",lst)

dictionary = {id: user for id, user in zip(ids, user)}
print("dictionary",dictionary)

# Функция zip пробегает по минимальному набору данных

salary = [111, 222, 333,444]
bonus = [1.1, 1.2]
short_list = list(zip(ids,user,salary,bonus))

print("list of minimum enteries",short_list)


#enumerate
print("enumerate->")
data_enumerate = list(enumerate(user))
print(data_enumerate)

fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(index, fruit)