def ValidAnagram(s,t):
    char_list = [0]*26

    for i in s:
        pos = ord(i) - ord('a')
        char_list[pos] += 1
    for j in t:
        pos = ord(j) - ord('a')
        char_list[pos] -= 1

    for k in char_list:
        if k !=0 :
            return False
    return True

print(ValidAnagram("abc","cba"))

#shortcut

def valid_Anagram(s,t):
    return sorted(s) == sorted(t)

print(valid_Anagram("abc","cba"))