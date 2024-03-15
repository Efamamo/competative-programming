class Solution(object):
    def minEatingSpeed(self, piles, h):
        def works(cand):
            res = 0
            for i in range(len(piles)):
                if piles[i]%cand:
                    res += piles[i]//cand+1
                else:
                    res += piles[i]//cand
            return res <= h
        l,r = 1,sum(piles)
        while l < r:
            m = (l+r)//2
            if works(m):
                r =m
            else:
                l = m+1
        return l



        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        