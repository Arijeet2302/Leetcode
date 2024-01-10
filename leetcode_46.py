class Solution:

    ans=[]
    ds = []

    def recurPermute(self, nums, freq):
        if len(self.ds) == len(nums):
            self.ans.append(list(self.ds))
            return
        
        for i in range(len(nums)):
            if not freq[i]:
                self.ds.append(nums[i])
                freq[i] = 1
                self.recurPermute(nums, freq)
                freq[i] = 0
                self.ds.pop()


    def permute(self, nums):
        self.ans = []
        self.ds = []
        freq = [0] * len(nums)
        self.recurPermute(nums, freq)
        return self.ans
    
obj = Solution()
print(obj.permute([1,2,3]))