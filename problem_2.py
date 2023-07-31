
def soln(arr):
    n=len(arr)
    for  i in range(n):
        for j in range(n-1-i):
            if arr[j]>=arr[j+1]:
                arr.pop(j+1)
    return arr



l1=[1,1,2,2,4,4]
print(soln(l1))