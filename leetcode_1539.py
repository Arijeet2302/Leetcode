def KthMissingNumber(arr,k):

    num=1
    temp=[]
    i=0

    while i<len(arr):
        if num!=arr[i]:
            temp.append(num) #adding missing numbers in queue
            num+=1
        else:
            i+=1
            num+=1

    #checking if temp is empty or not
    try:
        return temp[k-1] #if not then kth element
    except:
        return num + (k-1-len(temp)) #if yes then adding kth element to the num

print(KthMissingNumber([5,6,7,8,9],9))