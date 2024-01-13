
def findArraySum(a, n, b, m):
    # Write your code here.
    i = n-1
    j = m - 1
    carry = 0
    arr=[]

    while i>=0 and j >= 0:
        sum = a[i] + b[j] + carry
        arr.insert(0,sum%10)
        carry = sum // 10
        i-=1
        j-=1
    
    if i>=0:
        while i >=0:
            sum = a[i]+carry
            arr.insert(0,sum%10)
            carry = sum // 10
            i-=1
    elif j>=0:
        while j>=0:
            sum = b[j]+carry
            arr.insert(0,sum%10)
            carry = sum // 10
            j-=1
    elif carry != 0:
        arr.insert(0,carry)
    else:
        return arr
    return arr
        
a=[1,2,3,4]
n = len(a)
b = [6]
m = len(b)        
print(findArraySum(a,n,b,m))

# [ 1, 2, 3, 4]
#           [6]
# [ 1, 2, 4, 0]