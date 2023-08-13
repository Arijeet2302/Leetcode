def ValidPalindrome(s):
    s=s.lower()
    s1=""
    for i in s:
        asc=ord(i)
        if (asc >=97 and asc <=122) or (asc>=48 and asc <=57):
            s1+=i
    s2=s1[::-1]
    return s1==s2

print(ValidPalindrome("A man, a plan, a canal: Panama"))