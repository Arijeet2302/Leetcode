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

    def SwapPairs(self):
        temp = self.head
        if temp is None or temp.next is None:
            return 
        
        new_head = temp.next
        prev = None
        current = temp

        while current is not None and current.next is not None:
            next = current.next
            current.next = next.next
            next.next = current

            if prev :
                prev.next = next
            
            prev = current
            current = current.next

        self.head = new_head
    
        

ob=LL()
arr1=[1,2,3,4,5,6]
for i in arr1:
    ob.create(i)
ob.show()
ob.SwapPairs()
ob.show()



