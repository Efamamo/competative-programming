class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr =0
        largest = float("-inf")
        for r in range(len(nums)):
            
            if curr <0:
                curr = 0
            curr+= nums[r]
            largest = max(largest,curr)
        return largest
        