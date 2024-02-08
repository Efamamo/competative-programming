class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1

        res=[1]*len(nums)

        for i in range(len(nums)):
            res[i]*=pre
            res[len(nums)-i-1]*=post
            pre*=nums[i]
            post*=nums[len(nums)-i-1]
            
            
        return res

        