class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def helper(cand):
            res = 0
            for i in nums:
                if i%cand:
                    res += (i//cand)+1
                else:
                    res += (i//cand)
            return res <= threshold
        l,r = 1,2**32
        while l<r:
            m = (l+r)//2
            if helper(m):
                r = m
            else:
                l = m+1
        return l
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        