class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count={0:0,1:0}
        l=0
        max_l=0
        if 0 not in nums:
            return len(nums)-1

        for r in range(len(nums)):
            count[nums[r]]+=1
            if count[0]>1:
                count[nums[l]]-=1
                l+=1

            max_l=max(max_l,count[1])
        return max_l
            




                
        