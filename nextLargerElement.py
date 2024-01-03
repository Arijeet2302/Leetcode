def nextLargerElement(arr,n):
    res=[]
    stk=[]

    for i in range(n-1,-1,-1):
        if len(stk) == 0:
            res.append(-1)
            stk.append(arr[i])
        else:
            while len(stk) != 0 and arr[i]>=stk[-1]:
                stk.pop()        
            if len(stk) == 0:
                stk.append(arr[i])
                res.insert(0,-1)
                
            if arr[i] < stk[-1]:
                res.insert(0,stk[-1])
                stk.append(arr[i])
    return res

print(nextLargerElement([11,7,3,7,15],5))