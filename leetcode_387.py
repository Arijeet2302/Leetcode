def first_unique(s):
    pos=-1
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            pos=i
            break
    return pos        

s="leetcode"
print(first_unique(s))