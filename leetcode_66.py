def soln(l1):
    n=0
    l2=[]
    for i in l1:
        n=n*10+i
    n=n+1
    n=str(n)
    for i in n:
        l2.append(int(i))
    return l2
l1=[9]
print(soln(l1))
