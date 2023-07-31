def leftRightDifference(nums):
    left=[0]*len(nums)
    right=[0]*len(nums)
    l_sum=l=0
    r_sum=0
    r=len(nums)-1
    while r!=-1:
        left[l]=l_sum
        right[r]=r_sum
        l_sum+=nums[l]
        r_sum+=nums[r]
        l+=1
        r-=1
    for i in range(len(left)):
        left[i]=abs(left[i]-right[i])
    return left

print(leftRightDifference([10,4,8,3]))