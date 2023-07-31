def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        # we get a zero whenever we multiply with 5 i.e 5*2=10
        count=0
        while n>0:
            n//=5
            count+=n
        return count

print(trailingZeroes(5))