def sorted_square(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]**2
    arr.sort()
    return arr
arr=[-7,-3,2,3,11]
print(sorted_square(arr))