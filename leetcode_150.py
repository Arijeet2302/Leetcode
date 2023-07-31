def Evaluate_postfix(tokens):
    arr=[0]*len(tokens)
    top=-1
    for i in tokens:
        if i == '+' or i=='-' or i=='*' or i=='/':
            a=int(arr[top])
            b=int(arr[top-1])
            top-=2
            if i=='+':result=b+a
            elif i =='-':result=b-a
            elif i =='*':result=b*a
            else:
                if a*b >=0:result=b//a
                else: result=-(-b//a)
            top+=1
            arr[top]=result
        else:
            top+=1
            arr[top]=int(i)
    return arr[top]

print(Evaluate_postfix(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))