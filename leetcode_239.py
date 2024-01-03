from collections import deque
def MaxSlidingWindow(arr,k,n):
    res=[]
    max_queue = deque()

    for i in range(n):
        while max_queue and max_queue[0] < i-k+1:
            max_queue.popleft()

        while max_queue and arr[max_queue[-1]] < arr[i]:
            max_queue.pop()
        
        max_queue.append(i)

        if i >= k-1:
            res.append(arr[max_queue[0]])
    return res


res = MaxSlidingWindow([1,3,-1,-3,5,3,6,7],3,8)
print(res)