def good_pairs(arr):
    count=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count+=1
    return count

print(good_pairs([1,2,3,1,2,3]))