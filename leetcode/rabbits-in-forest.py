class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        
        res = 0
        for i in count:
            while count[i]>0:
                res += i+1
                count[i] -= (i+1)
            
        return res
            
            
        