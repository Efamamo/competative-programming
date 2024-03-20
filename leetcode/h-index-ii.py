class Solution(object):
    def hIndex(self, citations):
        l,r = 0,len(citations)-1
        if citations[r] <= 0:
            return 0
        while l<r:
            h = (l+r)//2
            if citations[h] < len(citations)-h:
                l = h+1
            else:
                r = h
        return len(citations)-l

        """
        :type citations: List[int]
        :rtype: int
        """
        