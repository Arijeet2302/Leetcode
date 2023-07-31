def remove_dups(nums):
    dup=list(set(nums))
    nums.sort()
    dup.sort()
    return not(dup == nums)

print(remove_dups([1,2,3,1]))