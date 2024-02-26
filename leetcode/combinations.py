class Solution(object):
    def combine(self, n, k): 
        res = []
        def backtrack(candidate):
            if len(candidate) == k:
                res.append(candidate[:])
            
            last = candidate[-1] if candidate else 0
            for next_last in range(last+1,n+1):
                candidate.append(next_last)
                backtrack(candidate)
                candidate.pop()
        backtrack([])
        return res

        

        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        