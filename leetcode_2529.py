def maxcount(nums):
    
    low=0
    high=len(nums)-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid] == 0:
            if nums[low]==0 and nums[high]==0: 
                break
            elif nums[low]==0: 
                high-=1
            elif nums[high]==0: 
                low+=1 
            else: 
                low+=1
                high-=1
        elif nums[mid]<0:
            low=mid+1
        else:
            high=mid-1

    negetiive=low
    positive=len(nums)-(high+1)

    return max(negetiive,positive)

print(maxcount([-3,-2,-1,0,0,1,2]))
