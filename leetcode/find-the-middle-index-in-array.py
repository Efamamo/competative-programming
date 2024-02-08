class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        curr = 0
        for i in range(len(nums)):
            tot-=nums[i]
            if curr == tot:
                return i
            curr += nums[i]
        return -1

            
        