class Solution(object):
    def searchInsert(self, nums, target):
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if l == len(nums)-1 and nums[l] < target:
            return l+1
        return l
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        