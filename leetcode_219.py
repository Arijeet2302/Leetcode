def dups(nums,k):
    arr={}
    for i in range(len(nums)):
        if nums[i] not in arr:
            arr[nums[i]]=i
        else:
            if i - arr[nums[i]] <=k:
                return True
            arr[nums[i]] = i
    return False

print(dups([1,2,3,1,2,3],2))