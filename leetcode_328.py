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
            

    def OddEvenList(self):
        if self.head is None:
            return
        temp = self.head
        temp1 = self.head.next
        even = temp1
        while temp.next :
            temp.next = temp.next.next
            temp = temp.next
            if temp is not None:
                temp1.next = temp.next
                temp1 = temp1.next
            else:
                temp1.next = None
                temp = temp1

        if temp == temp1:
            tempo = self.head
            while tempo.next:
                tempo = tempo.next
            tempo.next = even
        else:
            temp.next = even


ob = SLL()
arr=[1,2,3,4]
for i in arr:
    ob.create(i)
ob.show()
ob.OddEvenList()
ob.show()

