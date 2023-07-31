def soln(l1):
    arr=[0]
    arr[0]=l1[0]
    for i in l1:
        if arr[-1]!=i:
            arr.append(i)
    return arr
l1=[1,1,2]
print(soln(l1))