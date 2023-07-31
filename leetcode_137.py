#Mathematics set calculation with 41ms runtime
def single_numberII(nums):
    d=list(set(nums))
    sum1=sum(nums)
    sum2=3*(sum(d))
    return (sum2-sum1)/2


#Simple Array calculation with 800ms+ time
def single_numberI(nums):
    for i in nums:
        if nums.count(i)==1:
            return i
        
print(single_numberI([2,2,3,2]))
print(single_numberII([2,2,3,2]))