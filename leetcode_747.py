def DominantIndex(arr):
    max_num=max(arr)
    for i in arr:
        if i== max_num:
            continue
        if i*2 > max_num:
            return -1
    return arr.index(max_num)

arr=[1,3,6,0]
print(DominantIndex(arr))