
def productExceptSelf(nums):

    n = len(nums)
    result = [1] * n

    left_product = right_product = 1

        
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]

        
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

print(productExceptSelf([1,2,3,4]))