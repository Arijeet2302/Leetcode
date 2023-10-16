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
            

    def RemoveElements(self,val):
        temp = self.head
        prev = self.head
        while temp:
            if temp.value == val:
                if temp == self.head:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
                


ob = SLL()
arr=[1,2,2,1]
for i in arr:
    ob.create(i)
ob.show()
ob.RemoveElements(2)
ob.show()

