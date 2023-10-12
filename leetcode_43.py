def multiply(num1,num2):
    std = 48 
    res = 0
    count = 0
    for i in range(len(num1)-1,-1,-1):
        carry = 0
        current_num = 0
        place = 0
        for j in range(len(num2)-1,-1,-1):
            n1 = ord(num1[i]) - std
            n2 = ord(num2[j]) - std
            current_num  += ((n1*n2)%10 + carry) * (10**place)
            carry = (n1*n2)//10
            place +=1
        current_num += carry * (10**place)
        print(current_num)
        res += current_num * (10 **count)
        count+=1
    return str(res)

print(multiply("123","456"))