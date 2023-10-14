class Solution(object):
    def missingNumber(self, nums):
        num=[0]* (len(nums)+1)
        for i in nums:
            num[i]+=1
        for i in range(len(num)):
            if num[i]==0:
                return i
        

        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
