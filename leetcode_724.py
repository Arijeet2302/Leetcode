def pivot_element(arr):  #Time limit exceed
    pivot=0
    while pivot<len(arr):
        sum1=sum2=0
        for i in range(pivot):
            sum1+=arr[i]
        for j in range(pivot+1,len(arr)):
            sum2+=arr[j]
        if sum1==sum2:
            return pivot
        else:
            pivot+=1
    return -1

def pivot_element_fast(nums):  #Faster technique
    total= sum(nums)
    temp = 0
    for i in range(len(nums)):
        if(nums[i] == total - 2*temp): 
            return i
        temp += nums[i]
    return -1

arr=[1,7,3,6,5,6]
print(pivot_element(arr))
print(pivot_element_fast(arr))