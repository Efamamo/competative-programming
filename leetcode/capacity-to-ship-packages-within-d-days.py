class Solution(object):
    def shipWithinDays(self, weights, days):
        def works(capacity,days):
            i = len(weights)-1
            val = capacity
            while i >= 0:
                while i >= 0 and val - weights[i] >= 0:
                    val -= weights[i]
                    i -= 1
                days -=1
             
                val = capacity
            return days >= 0
        
        l, h = max(weights), sum(weights)
        while l < h:
            m = (l + h) //2
            if works(m,days):
                h = m
            else:
                l = m+1
        return l

        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        