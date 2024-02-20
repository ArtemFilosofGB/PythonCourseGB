import sqlite3


#Sum digits alse return 0
def sum_array(a):
    sum=0
    for num in a:
        try:
            sum+=int(num)
        except:
            return 0
    return sum

a=[1,2,3,0.1,5]
print(sum_array(a))