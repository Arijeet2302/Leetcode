def slon(n):
    sum=0
    rev=0
    for i in range(1,n+1):
        sum+=i
        for j in range(n,i+1,-1):
            rev+=j
    if rev==sum:
        return i

print(slon(8))