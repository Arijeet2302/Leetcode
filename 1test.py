s="0P"
s=s.lower()
s1=""
for i in s:
    asc=ord(i)
    if (asc >=97 and asc <=122) or (asc>=48 and asc <=57):
        s1+=i
print(s1)