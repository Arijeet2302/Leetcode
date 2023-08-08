def ReverseWord(s):
    s=s.strip() #trimming the string
    s=list(s) 

    arr=[]
    temp=""
    for i in s: # adding all the words in a list
        if i==" ":
            arr.append(temp)
            temp=""
        else: temp+=i

    arr.append(temp)


    arr = list(filter(lambda x: x != '', arr)) #filtering extra spaces
    arr=arr[::-1]


    str1=""
    for i in arr:
        str1+=i
        str1+=" "


    return str1.rstrip()

print(ReverseWord("sky is blue"))