class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        res = ["bad"]*len(nums)
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= last:
                res[i] = "good"
                last = i
        return res[0] == "good"

        