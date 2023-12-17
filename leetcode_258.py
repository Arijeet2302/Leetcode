def addDigits(n):
    if n // 10 == 0:
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