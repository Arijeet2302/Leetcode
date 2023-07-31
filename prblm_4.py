class soln:
    def show(self,x):
        self.x=x
        self.y=str(self.x)
        if self.y[0]=="-":
            self.y=self.y[:0:-1]
            return  int("-"+self.y)
        else:
            self.y=self.y[::-1]
            return int(self.y)
         
        
ob=soln()
x=int(input("Enter number:"))
print(ob.show(x))

#not complete leetcode Qno. 7