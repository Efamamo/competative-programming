class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        if x < 2:
            return x
        while l < r:
            m = (l+r)//2
            if m*m <= x:
                l = m+1
            else:
                r = m
        return l-1
        """
        :type x: int
        :rtype: int
        """
        