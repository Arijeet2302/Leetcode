def soln(x):
    a=2**31
    n=x
    if x<0:
        x=str(x)
        rev="-"+x[:0:-1]
    else:
        x=str(x)
        rev=x[::-1]
    if n < -a and n > (a-1):
        return 0
    else:
        return rev
    
print(soln(1534236469))