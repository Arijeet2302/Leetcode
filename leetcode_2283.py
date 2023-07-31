def digit_count(num):
    f=0
    for i in range(len(num)):
        if num.count(str(i)) == int(num[i]):
            f=1
        else:
            f=0
            break
    if f==1:return True
    else:return False

print(digit_count("1210"))