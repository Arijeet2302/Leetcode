def countPs(s, start, end):
    if start == end:
        return 1

    if start > end:
        return 0

    if s[start] == s[end] :
        return 1 + countPs(s,start+1,end) + countPs(s,start,end-1)
    else:
        return countPs(s,start+1,end) + countPs(s,start,end-1) - countPs(s,start+1 ,end-1)

tc = int(input())
for _ in range(tc):
    s=input()
    res = countPs(s,0,len(s)-1)
    print(res)