def PowerOfThree(n):
    num=0
    if n<0:
        return False
    else:
        while num!=n:
            num*=3
            if num>3:
                return False
    return True

print(PowerOfThree(27))