def soln(arr,n):
    l1=[]
    start=0
    mid=n//2
    while start<=(n//2) and mid<=n-1:
        l1.append(arr[start])
        l1.append(arr[mid])
        start+=1
        mid+=1
    return l1

#def with recursion
def soln_recursion(arr,l1=[],start=0):
    n=len(arr)
    mid=start+n//2
    if start < n//2 and mid < n:
        l1.append(arr[start])
        l1.append(arr[mid])
        start+=1
        return soln_recursion(arr,l1,start)
    return l1



arr=[1,2,3,4,5,6,7,8]
print(soln(arr,len(arr)))
print(soln_recursion(arr))