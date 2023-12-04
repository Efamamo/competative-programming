class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count=0
        count=0
        for r in range(len(nums)):
            if nums[r]==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count


        """
        :type nums: List[int]
        :rtype: int
        """
        