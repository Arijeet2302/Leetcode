def add_list(num,k):
    sum=0
    for i in num:
        sum=sum*10+i
    sum=sum+k
    arr=[]
    while sum:
        rem=sum%10
        arr.append(rem)
        sum//=10
    arr.reverse()
    return arr

print(add_list([1,2,0,0],34))  