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
            

    def ReverseList(self):
        p=None
        current=self.head
        if current is None:
            return
        q=current.next
        while q:
            current.next=p
            p=current
            current=q
            q=q.next
        current.next=p
        self.head=current
                


ob = SLL()
arr=[1,2,2,1]
for i in arr:
    ob.create(i)
ob.show()
ob.ReverseList()
ob.show()

