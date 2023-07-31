def Hexadecimal(num):
    s=""
    if num==0:
        return "0"
    if num<0:
        num=num+2**32
    while num!=0:
        a=num%16
        if a>9:
            a=chr(a+87)
        s+=str(a)
        num=num//16
    return s[::-1]


num=-1
print(Hexadecimal(num))