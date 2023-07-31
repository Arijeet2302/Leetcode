def LengthOfLastWord(s1):
    s1=s1.strip()
    count=0
    i=-1
    var=s1[i] #last char
    
    
    #counting until a space occurs
    while var!=" ":
        count+=1
        i-=1
        var=s1[i]
    return 


print(LengthOfLastWord(" fly me   to  moon  "))