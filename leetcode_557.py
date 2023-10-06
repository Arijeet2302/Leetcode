def ReverseWord(s):
    res = s.split()
    temp=""
    for i in res:
        rev=i[::-1]
        temp += rev + " "
    temp = temp.strip()
    return temp

print(ReverseWord("Ram is a good boy"))