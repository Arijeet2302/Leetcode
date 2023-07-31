def addDigits(n):
    if len(str(n))==1:
        return n
    else:
        sum=0
        while n!=0:
            a=n%10
            sum+=a
            n/=10
        return addDigits(sum)
    
num=38
print(addDigits(num))