def soln(arr):
    for i in arr:
        if arr.count(i)!=2:
            return i
arr=[4,1,2,2,1]
print(soln(arr))