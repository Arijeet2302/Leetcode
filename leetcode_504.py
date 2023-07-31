def Base_7(num):
    s=""
    n=num 
    if num==0:
        return "0"       
    while abs(num)!=0:
        a=abs(num)%7
        s+=str(a)
        num=abs(num)//7
    if n<0:
        s=s+'-'
    s=s[::-1]
    return s
print(Base_7(-7))