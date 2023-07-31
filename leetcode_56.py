def intervals(arr):
    i=0
    while i < len(arr)-1:
        j=i+1
        print(arr,i,j)
        if arr[i][0] >= arr[j][0]:
            arr[i][0]=arr[j][0]
            arr.remove(arr[j])
        elif arr[j][-1]>= arr[i][-1] and arr[j][0]<= arr[i][-1]:
            arr[i][-1]=arr[j][-1]
            arr.remove(arr[j])
        else:
            pass
        i+=1
    return arr

print(intervals([[1,4],[1,5]]))

#Not accepted
