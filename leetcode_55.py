def PowerofTwo(n):
    if n<0:
        return False
    if n==1:
        return True
    elif n%2==0:
        return False
    elif n==0 or n==3 or n==5 or n==9:
        return False
    else:
        n=n//2
        return PowerofTwo(n)
    
print(PowerofTwo(17))