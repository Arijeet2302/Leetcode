def divisor_game(n):
    alice=0
    i=1
    while n!=1:
        if n%i==0:
            n=n-i
            alice+=1
        else:i+=1
    if alice % 2 == 0:return False
    else:return True

print(divisor_game(3))