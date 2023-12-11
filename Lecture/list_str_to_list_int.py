
#Строка String
data= '14 1424 12 1 9 123412'
print(data)

#List of strings
data= data.split()
print(data)

#using map to use Int to list of strings - data
data = list(map(int, data))
print(data)