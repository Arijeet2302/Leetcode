def maxArea(arr):
    start=0
    end=len(arr)-1
    area=0 #Total area

    while start<end:

        ht=min(arr[start],arr[end]) #height of rectangle 
        width=abs(start-end)    #width of rectangle
        current_area=ht*width #calculating current area

        if current_area > area:
            area=current_area
        
        if arr[start] < arr [end]: #converging rectangle to larger area
            start+=1
        else:
            end-=1

    return area


print(maxArea([1,8,6,2,5,4,8,3,7]))