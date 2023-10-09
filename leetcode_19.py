class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
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

    def RemoveFromNthLast(self,k):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp=self.head
        prev=None
        for i in range(count-k):
            prev=temp
            temp=temp.next
        next = temp.next

        if count==1:
            self.head = None
            return
        
        if next is None:
            prev.next=None
        elif prev is None:
            self.head = next
        else:
            prev.next = next


        

ob=LL()
arr=[1,2]
for i in arr:
    ob.create(i)
ob.show()
ob.RemoveFromNthLast(2)
ob.show()



