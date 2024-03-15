class Solution(object):
    def searchRange(self, nums, target):
        def s(val):
            l , r = 0, len(nums)
            while l < r:
                m = (l+r)//2
                if nums[m] < val:
                    l = m+1
                else:
                    r = m
            return l
        l = s(target)
        r = s(target+1)-1

        return [l,r] if l<=r else [-1,-1]
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        