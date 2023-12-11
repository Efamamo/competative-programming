class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        order={}
        for l,r in enumerate(nums):
            order[r]=l
        for i,j in operations:
            nums[order[i]]=j
            order[j]=order[i]
        return nums


        