def soln(n):
    if n==1:
        return True
    arr=[]
    while n!=1:
        for i in range(2,n):
            if n%i==0:
                arr+=[i]
                n=n//i
    print(arr)
    for i in arr:
        if prime(i) is False:
            arr.remove(i)
    print(arr)
    nums=set(arr)-{2,3,5}
    nums=list(nums)
    if len(nums)!=0:
        return False
    else:
        return True
        
def prime(n):
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break
        else:
            f=0
    if f==0:
        return True
    else:
        return False

n=-2147483648
# print(soln(n))

#good solution but having space complexity problems
#so alternative easy method

def isUgly(n):
    for p in 2, 3, 5:
        while n % p == 0 and p < n:
            n /= p
    return n == 1

print(isUgly(n))