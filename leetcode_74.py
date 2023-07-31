def search_matrix(arr,s):
    f=1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if s == arr[i][j]:
                f=0
                break
    if f==1:
        return False
    else:
        return True
    
arr=[[1,3,4,56],[23,242,221],[526,516]]
print(search_matrix(arr,23))