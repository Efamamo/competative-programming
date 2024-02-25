class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            j = i-1
            k = 0
            while k < j:
                if nums[j]+nums[k] <= nums[i]:
                    k += 1
                else:
                    res += (j-k)
                    j-=1      
        return res
                    
                    
        