def FindDistanceValue(arr1,arr2,d):
    count=0
    for i in arr1:
        f=0
        for j in arr2:
            if abs(i-j)>d:
                f=1
            else:
                f=0
                break
        if f==1:
            count+=1

    return count

arr1=[4,5,8]
arr2=[10,9,1,8]
d=2
print(FindDistanceValue(arr1,arr2,d))