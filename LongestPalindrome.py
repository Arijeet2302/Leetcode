class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) <= 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1: right]

        max_pal = s[0]

        for i in range(len(s)-1):
            odd = expand(i, i)
            even = expand(i, i+1)

            if len(odd) > len(max_pal):
                max_pal = odd

            if len(even) > len(max_pal):
                max_pal = even

        return max_pal
