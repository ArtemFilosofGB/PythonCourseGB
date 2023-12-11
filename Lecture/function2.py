def sum_str(*args):
    res = ''
    for i in args:
        res+=i
    return res

def sum_int(*args):
    res = 0
    for i in args:
        res+=i
    return res

print(sum_str("q","w",'e','r','t','y'))
print(sum_int(1,2,3,4,5,6,7,8,9,10))