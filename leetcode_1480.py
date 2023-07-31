def running_sum(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        arr[i]=sum
    return arr

print(running_sum([1,2,3,4,5]))