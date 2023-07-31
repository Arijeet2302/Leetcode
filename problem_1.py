#find the Kth smallest element in the given array
class solution:
    def sort(self,arr,n):
        self.n=n
        self.arr=arr
        for i in range(self.n-1):
            self.min=i
            for j in range(i+1,self.n):
                if self.arr[self.min]>self.arr[j]:
                    self.min=j
            self.arr[i],self.arr[self.min]=self.arr[self.min],self.arr[i]
        return self.arr
    def result(self,k):
        self.k=k
        return self.arr[self.k-1]
ob=solution()
m=int(input("Enter size of list:"))
lst=[0]*m
for i in range(m):
    lst[i]=int(input())
k=int(input("Enter the smallest element to search:"))
print(lst)
ob.sort(lst,m)
print("element is:",ob.result(k))