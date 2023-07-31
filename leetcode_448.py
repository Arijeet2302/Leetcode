def disappeared_num(nums):
    nums.sort()
    num=1
    l1=[]
    while num<=len(nums):
        if binary(nums,len(nums),num) == -1:
            l1.append(num)
        num+=1
    return l1

def binary(arr,n,s):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<s:
            low=mid+1
        elif arr[mid]>s:
            high=mid-1
        else:
            return mid
    return -1

print(disappeared_num([1,1])) 