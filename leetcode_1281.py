def subtractProductAndSum(n):
    product=1
    sum1=0
    while n!=0:
        rem=n%10
        product*=rem
        sum1+=rem
        n//=10
    return product-sum1
print(subtractProductAndSum(234))