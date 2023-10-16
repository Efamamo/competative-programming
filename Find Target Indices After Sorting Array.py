class Solution(object):
    def targetIndices(self, nums, target):
        num=sorted(nums)
        result=[]
        for i,e in enumerate(num):
            if e==target:
                result.append(i)
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
