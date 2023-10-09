def searchRange(nums, target):
    low = 0
    high = len(nums) - 1
    start = end = -1

    # Binary search for the start index
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            start = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    # Binary search for the end index
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            end = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if start > end:
        return [-1, -1]
    else:
        return [start, end]
    

print(searchRange([5,7,7,8,8,10],8))
