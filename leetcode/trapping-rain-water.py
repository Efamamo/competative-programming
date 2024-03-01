class Solution:
    def trap(self, height: List[int]) -> int:
        maxim = 0
        left = [0]*len(height)
        for i in range(len(height)):
            left[i] = maxim
            maxim = max(maxim,height[i])
        
        maxim = 0
        right = [0]*len(height)
        for i in range(len(height)-1,-1,-1):
            right[i] = maxim
            maxim = max(maxim,height[i])
        for i in range(len(height)):
            height[i] = min(left[i],right[i])-height[i]
        
        res = 0
        for i in height:
            if i>0:
                res+=i
        return res