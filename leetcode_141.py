class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    
    def create(self,n):
        new = Node(n)
        if self.head == None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new

    def show(self):
        temp=self.head
        if self.head is None:
            print("empty")
        while temp:
            print(temp.value,end=" ")
            temp=temp.next
        print()
            

    def hasCycle(self):
        temp = self.head
        while temp:
            if temp.value == " ":
                return True
            temp.value = " "
            temp = temp.next 
        return False
                


ob = SLL()
arr=[3,2,0,4]
for i in arr:
    ob.create(i)
print(ob.hasCycle())

