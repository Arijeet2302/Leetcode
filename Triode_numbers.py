
def FindTriodeNum(start,end):

    for num in range(start, end+1):
            
        digits = []

        for i in range(1, 4):
            x = i * num

            while x > 0:
                rem = x % 10
                if rem not in digits:
                    digits.append(rem)
                    x //= 10
                else:
                    break

            if x != 0:
                break
                
        if x == 0:
            print (num)

print("Listed Triode Numbers :")
FindTriodeNum(102 , 498)
