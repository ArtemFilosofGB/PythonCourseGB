d = {}
d = dict()
d['q']='qwerty'
print(d)

d['w']="weather"
print(d)
print(d['w'])
d[123]=1234567
print(d)
print(d[123])

del d['q']
print(d)

d["qwe"]="qwertyqwerty"

for item in d:
    print("{}:{}".format(item,d[item]))

print(d.items())
for (k,v) in d.items():
    print(k,v)
