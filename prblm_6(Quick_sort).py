def partition(arr,low,high):
    pivot=arr[high]

    i=low-1


    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1

            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1       

def quick(arr,low,high):
    if low< high:

        pi=partition(arr,low,high)

        quick(arr,low,pi-1)#for left elements
        quick(arr,pi+1,high)#for right elements

l1=[1,2,5,3,98,4,7]
quick(l1,0,len(l1)-1)
print(l1)