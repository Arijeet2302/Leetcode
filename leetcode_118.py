def soln(n):
    if n==1:
        return [[1]]
    if n==2:
        return [[1],[1,1]]
    lst=[[1],[1,1]]
    for i in range(3,n+1):
        current=lst[-1]
        current.append(0)
        for i in range(len(current)-2):
            n=current[i]+current[i+1]
            current[-1]=current[i+1]
            current[i+1]=n
        lst.append(current)
    return lst

n=5
print(soln(n))