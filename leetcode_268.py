def soln(arr):
    arr.sort()
    n=len(arr)+1
    l=[]
    for i in range(n):
        l.append(i)
    num=set(l)-set(arr)
    return list(num)[0]
arr=[0,1]
print(soln(arr))