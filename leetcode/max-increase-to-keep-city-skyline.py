class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        val = [[0]*len(grid),[0]*len(grid)]
    
        res = 0
        for i in range(len(grid)):
            maxim = max(grid[i])
            val[0][i] = maxim
            
                 
        for i in range(len(grid)):
            maxim = float("-inf")
            for j in range(len(grid)):
                maxim = max(grid[j][i],maxim)
            val[1][i] = maxim
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += min(val[0][i],val[1][j])-grid[i][j]
                
        return res
    
        
        
        
        
        
                
        