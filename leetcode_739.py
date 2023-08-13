def DailyTemp(arr):
    n = len(arr)
    temp = [0] * n  # Initialize the temp list with zeros
    stack = []      # Stack to store indices
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            prev_index = stack.pop()
            temp[prev_index] = i - prev_index
        stack.append(i)
    
    return temp

print(DailyTemp([40,30,20,10]))