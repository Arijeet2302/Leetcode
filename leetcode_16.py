def threesumclosest(arr,target):
    arr.sort()
    
    initial_sum = arr[0] + arr[1] + arr[2]
    
    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1
        
        while start < end:
            val = arr[i] + arr[start] + arr[end]
            
            if abs(val - target) < abs(initial_sum - target):
                initial_sum = val
            if val < target:
                start +=1
            elif val > target:
                end-=1
            else:
                return target
    return initial_sum


print(threesumclosest([-1,2,1,-4],1))