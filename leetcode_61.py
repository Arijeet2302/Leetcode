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

    def rotate(self,k):
        if self.head is None or self.head.next is None:
            return 
        else:
            # making it a circular LL
            temp = self.head
            count = 1
            while temp.next:
                temp = temp.next
                count +=1
            temp.next = self.head


            current = self.head
            '''
            calculating the last node after rotation i.e.
            pos = total node - rotataion and it is from last position
            '''
            k = count - (k % count) 
            for _ in range(k-1):
                current = current.next
            self.head = current.next
            current.next = None # breaking the circular LL
                 

ob = SLL()
arr=[1,2,3]
for i in arr:
    ob.create(i)
ob.show()
ob.rotate(2000000000)
ob.show()