def soln(num1,num2):
    num1=binary(num1)
    num2=binary(num2)
    num3=num1+num2
    print(num3)
    print(num1)
    print(num2)
    num3=decimal(num3)
    return num3

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

n1=1010
n2=1011
print(soln(n1,n2))