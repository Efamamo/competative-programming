class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pre = 0
        res = 0
        i = 1
        j = 0
        while i <= n:
            while j < len(nums) and nums[j]<=i:
                pre += nums[j]
                j+=1
            if pre<i:
                res+=1
                pre += i
            i = pre + 1
       
        
        return res
        
        
                
        