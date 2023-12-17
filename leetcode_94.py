class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            temp = self.root
            while temp:
                if temp.left is None:
                    temp.left = Node(val)
                    break
                elif temp.right is None:
                    temp.right = Node(val)
                    break
                else:
                    if temp.left.val == 0:
                        temp = temp.right
                    else:
                        temp = temp.left


    def BinartTreeInorderTraversal(self):
        res=[]
        ptr = self.root
        stk = [0]

        while ptr != None :
            stk.append(ptr)
            ptr = ptr.left
        ptr = stk.pop()
        while ptr != 0:
            res.append(ptr.val)
            if ptr.right is not None:
                ptr = ptr.right
                while ptr != None :
                    stk.append(ptr)
                    ptr = ptr.left
            ptr = stk.pop()

        return res
    
arr=[1,0,2,3]
ob = Solution()
for i in arr:
    ob.insert(i)
res = ob.BinartTreeInorderTraversal()
print(res)