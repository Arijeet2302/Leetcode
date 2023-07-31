def sortArrayByParity(arr):
    low=0
    high=-1
    nums=[0]*len(arr)
    for i in arr:
        if i%2==0:
            nums[low]=i
            low+=1
        else:
            nums[high]=i
            high-=1
    return nums
print(sortArrayByParity([1,2,3,4]))