def Serach_RotatedArray(arr,k):
    max_num=max(arr)
    index=arr.index(max_num)
    left=arr[0:index+1]
    right=arr[index+1:]
    if left[0]<=k and k<=left[-1]:
        print(8)
        arr=left
        low=0
        high=len(arr)-1
        while low<=high:
                mid=(low+high)//2
                if arr[mid]<k:low=mid+1
                elif arr[mid]>k:high=mid-1
                else:return mid
        return -1
    else:
        arr=right
        low=0
        high=len(arr)-1
        while low<=high:
                mid=(low+high)//2
                if arr[mid]<k:low=mid+1
                elif arr[mid]>k:high=mid-1
                else:return mid+(index+1)
        return -1

print(Serach_RotatedArray([1,3],1))