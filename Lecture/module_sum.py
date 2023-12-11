def max1(a,b):
    if(a>b):
        return a
    return b

def fibonachi(n):
    if n in [1,2]:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)