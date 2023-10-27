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
            

    def MiddleOFLinkedList(self):
        temp = self.head
        count = 1
        while temp.next:
            temp = temp.next
            count +=1

        temp =self.head
        if count % 2 != 0:
            for _ in range(count//2):
                temp = temp.next
        else:
            for _ in range(count//2):
                temp = temp.next
        
        self.head = temp


ob = SLL()
arr=[1,2,3,4,5]
for i in arr:
    ob.create(i)
ob.show()
ob.MiddleOFLinkedList()
ob.show()

