def self_Divide(num):
    temp=num
    count=0
    while temp:
        rem=temp%10
        if rem!=0:
            if num%rem==0:
                count+=1
        temp//=10
    return count

print(self_Divide(1234))