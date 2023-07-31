class soln:
    def show(self,x):
        self.x=x
        self.y=self.x.replace(":","").replace(" ","").replace(",","")
        self.y=self.y.lower()
        self.rev=self.y[::-1]
        if self.rev==self.y:
            return True
        elif self.rev==" ":
            return True
        else:
            return False

ob=soln()
x=input()
print(ob.show(x))