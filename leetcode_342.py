def PowerOfFour(n):
    num=1
    if n<0:
        return False
    else:
        while num!=n:
            num*=4
            if num>n:
                return False
    return True

print(PowerOfFour(64))