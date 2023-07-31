def soln(nums,n):
    i = 0
    for x in nums:
        if x != n:
            nums[i] = x
            i += 1
    return i


l=[3,2,2,4]
print(soln(l,2))