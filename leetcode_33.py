def Serach_RotatedArray(nums, target):
        low, high = 0, len(nums) - 1


        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid] and nums[low] <= target < nums[mid]:
                high = mid - 1
            elif nums[mid] <= nums[high] and nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                if nums[mid] <= nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1

print(Serach_RotatedArray([1,3],1))