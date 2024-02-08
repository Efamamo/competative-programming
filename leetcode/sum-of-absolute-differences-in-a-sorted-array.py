class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        val=[]
        total=sum(nums)
        current=0
        for i in range(len(nums)):
            current+=nums[i]
            val.append((i+1)*nums[i]-current+(total-current)-(len(nums)-i-1)*nums[i])
        return val
