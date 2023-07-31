def inter_section(num1,num2):
    num3=set(num1)&set(num2)
    return list(num3)

n1=[1,2,2,1]
n2=[2,2]
print(inter_section(n1,n2))