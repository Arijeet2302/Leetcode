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
            

    def RemoveDuplicate(self):
        if self.head is None:
            return
        else:
            temp = self.head
            value = None
            prev = None
            while temp:
                if temp.value == value:
                    prev.next = temp.next
                    temp = prev.next
                else:
                    prev = temp
                    value = prev.value
                    temp = temp.next


ob = SLL()
arr=[1,2,2,3,4,4,4,5,6,7,7]
for i in arr:
    ob.create(i)
ob.show()
ob.RemoveDuplicate()
ob.show()