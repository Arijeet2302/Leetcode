def moveZeroes(nums):
    if nums.count(0)!=0:
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                cur=nums[pos]
                nums[pos]=nums[i]
                nums[i]=cur
                pos+=1
    return nums

print(moveZeroes([1,0,3,12,0,0]))