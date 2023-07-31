def shuffleString(s,indices):
    s=list(s)
    indices1=[0]*len(s)
    for i in range(len(indices)):
        indices1[indices[i]]=s[i]
    str1=""
    for i in indices1:
        str1+=i
    return str1
print(shuffleString('codeleet',[4,5,6,7,0,2,1,3]))