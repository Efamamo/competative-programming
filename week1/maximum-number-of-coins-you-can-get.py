class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res=0
        k=len(piles)-len(piles)//3
        for i in range(1,k,2):
            res+=piles[i]
            

        
        return res
        