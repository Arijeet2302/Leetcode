def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        l=0
        u=x//2

        while l<=u:
            mid=l+(u-l)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l=mid+1
            else:
                u=mid-1
        return int(u)
print(mySqrt(50))