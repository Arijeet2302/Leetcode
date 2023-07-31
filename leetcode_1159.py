def DayofYear(s1):
    year=int(s1[0:4])
    month=int(s1[5:7])
    day=int(s1[8:])
    days=0
    for i in range(1,month):
        if i==2:
            days+=28
        elif i<8:
            if i%2==0:
                days+=30
            else:
                days+=31
        else:
            if i%2==0:
                days+=31
            else:
                days+=30
    days+=day
    if ((year%4==0 and year%100!=0) or ( year%400==0 and year%100==0)) and month>2:
        days+=1
    return days
s1="2019-01-19"
print(DayofYear(s1))