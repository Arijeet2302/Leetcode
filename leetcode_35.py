def soln(arr,n,item):
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if item<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return low

arr=[1,3,5,6]
print(soln(arr,len(arr)-1,5))