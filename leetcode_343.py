def IntegerBreak(n):
    
    if n==2 or n==3:
        return n-1
    
    result = 1
    while n>4:
        n-=3
        result*=3
    return result*n

print(IntegerBreak(10))