def RomanToInt(s):
    mydict = dict()
    res = 0

    keys = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    values = [1,4,5,9,10,40,50,90,100,400,500,900,1000] 

    for i in range(len(keys)):
        mydict[keys[i]] = values[i]

    for i in range(len(s)):
        if i < len(s)-1 and mydict[s[i]] < mydict[s[i+1]]:
            res -= mydict[s[i]]
        else:
            res += mydict[s[i]]
    print(res)

RomanToInt("MCMXCIV")