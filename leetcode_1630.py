def ArithmaticSubArray(nums,l,r):
    res=[]
    for i in range(len(l)):
        sub_array = nums[l[i]:r[i]+1]
        sorted_array = sorted(sub_array)
        gap = abs(sorted_array[1]-sorted_array[0])
        for j in range(len(sorted_array)-1):
            if abs(sorted_array[j]-sorted_array[j+1]) != gap:
                res.append(False)
                break
        else:
            res.append(True)    
    return res

print(ArithmaticSubArray([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7],[4,4,9,7,9,10]))