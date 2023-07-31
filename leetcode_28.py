def soln(str1,str2):
    k=str1.find(str2,0,len(str1))
    return k
s1="leetcode"
s2="leet"
print(soln(s1,s2))