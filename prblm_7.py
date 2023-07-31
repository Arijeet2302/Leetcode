
def soln(arr,n):
    arr.sort()
    arr1=[]
    for i in arr:
        if i not in arr1:
            arr1+=[i]
    return arr1[-2]
n=7
arr=[2,3,6,6,5,3,4]
print(soln(arr,n))    
    
