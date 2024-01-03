def soln(s): #ValidParenthesis
    arr=[0]*len(s)
    top=-1
    for i in s:
        if i == '(' or i == '{' or i == '[':
            top+=1
            arr[top]=i
        elif i == ')' and arr[top]=='(':
            top-=1
        elif i == '}' and arr[top]=='{':
            top-=1
        elif i == ']' and arr[top]=='[':
            top-=1
        else:
            return False
    if top==-1:
        return True 
    else:
        return False
    
s="(]"
print(soln(s))