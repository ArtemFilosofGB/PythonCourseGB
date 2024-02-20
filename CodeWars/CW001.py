#Sum without highest and lowest number
#If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

def sum_array(arr):
    #your code here
    if not arr or len(arr) == 1:
        return 0
    minn = 9999999
    maxx = -9999999
    summ = 0
    for item in arr:
        if item > maxx:
            maxx = item
        if item < minn:
            minn = item
        summ += item
    return summ - maxx - minn

a={1,2,3,4,5}
print(sum_array(a))