#Using Dynamic programming ( recursion + Memoization)

def fibo(n, arr):
    if n<=1:
        return n
    elif arr[n]!=-1:
        return arr[n]
    else:
        arr[n] = fibo(n-1,arr) + fibo(n-2,arr)
        return arr[n]

n=6
arr = [-1]*(n+1)
print(fibo(n,arr)) 