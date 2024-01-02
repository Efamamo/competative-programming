class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                
            i+=1
           
      
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """