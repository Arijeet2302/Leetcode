class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.keep = None

    def create(self,val):
        new = Node(val)
        if self.head is None:
            self.head = new
            self.keep = self.head
        else:
            self.keep.next = new
            self.keep = self.keep.next
    
    def show(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp:
                print(temp.val,end=" ")
                temp = temp.next
            print()

ob = SLL()
arr=[1,2,3,4,5]
for i in arr:
    ob.create(i)
ob.show()