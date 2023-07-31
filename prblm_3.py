class soln:
    def show(self,x):
        self.x=x
        self.y=str(self.x)
        if self.y[0]=="-":
            return False
        else:
            self.z=self.y[::-1]
            if int(self.z)==self.x:
                return True
            else:
                return False
            
ob=soln()
x=int(input("Enter number:"))
print(ob.show(x))
