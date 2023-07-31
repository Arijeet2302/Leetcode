def soln(arr,xtra):
    l1=[]
    for i in arr:
        if (i+xtra) >= max(arr):
            l1.append("true")
        else:
            l1.append("false")
    return l1

arr=[2,3,5,1,3]
xtra=3
print(soln(arr,xtra))