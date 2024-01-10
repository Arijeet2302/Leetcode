
class Solution:

    keep = ""
    ans=[]

    def permutations(self,s,freq):
        if len(self.keep)==len(s):
            self.ans.append(str(self.keep))
            return
        
        for i in range(len(s)):
            if not freq[i]:
                self.keep+=s[i]
                freq[i] = 1
                self.permutations(s,freq)
                freq[i] = 0
                self.keep=self.keep[:-1]

    def permute(self, s) :
        self.keep = ""
        self.ans=[]
        freq = [0]*len(s)
        self.permutations(s,freq)
        return self.ans
    
obj = Solution()
print(obj.permute("abc"))