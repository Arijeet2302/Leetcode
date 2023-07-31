# Hamming distance is the number of differnt bits between two numbers bit reprsentation
def HammingDistance(x,y):
    #calcualting XOR as XOR is "1" is bits are different
    num=x^y
    count=0
    while num!=0:
        rem=num%2
        if rem==1:
            count+=1
        num//=2
    return count

print(HammingDistance(14,2))
        