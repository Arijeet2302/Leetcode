def Happy_num(n):
    if n==1:
        return True
    elif n==4 :
        return False
    else:
        sum=0
        while n!=0:
            a=n%10
            sum+=a**2
            n=n//10
        return Happy_num(sum)
    


print(Happy_num(2))