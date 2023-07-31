def complement_binary(n):
    n=str(decimal(n))
    s=""
    for i in n:
        if i == '1':
            s+='0'
        else:
            s+='1'
    result=binary(int(s))
    return result

def binary(num):
    result=0
    i=0
    while num!=0:
        r=num%10
        result+=r*2**i
        i+=1
        num=num//10
    return result

def decimal(num):
    result=0
    i=0
    while num!=0:
        r=num%2
        result+=r*10**i
        num=num//2
        i+=1
    return result

num=5
print(complement_binary(num))