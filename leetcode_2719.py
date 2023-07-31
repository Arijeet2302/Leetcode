'''solved but not fast enough
faster technique due'''

def count(n1,n2,min,max):
    n1=int(n1)
    n2=int(n2)
    count1=0
    for i in range(n1,n2+1):
        s=sum_digits(i)
        # print(s)
        if s >= min and s <=max :
            count1+=1
    return count1

def sum_digits(n):
    sum=0
    while n!=0:
        a=n%10
        sum+=a
        n=n//10
    return sum

print(count("1","5",1,5))
