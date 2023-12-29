class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res=0
        nums.sort(reverse=True)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                res+=i+1
        return res




        