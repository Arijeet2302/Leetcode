def self_divide(left,right):
    arr=[]
    for i in range(left,right+1):
        num=i
        f=0
        while i:
            rem=i%10
            if rem!=0:
                if num%rem == 0 :
                    f=1
                else:
                    f=0
                    break
            else:
                f=0
                break
            i//=10
        if f==1:
            arr.append(num)
    return arr

print(self_divide(1,22))