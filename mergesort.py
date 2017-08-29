nums = [23,56,78,23,45,67,89,10,11,34,47,24,21,69,80]
def merge_sort(x):

    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))   
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result
    
    
output = merge_sort(nums)
print(output)


mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist[:5])
print(mylist[5:])