class Solution(object):
    def twoSum(self, nums, target):
        
        for i,e in enumerate(nums):
            nums[i] = [e,i]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i][0]+nums[j][0]==target:
                return [nums[i][1],nums[j][1]]
            elif nums[i][0]+nums[j][0]>target:
                j-=1
            else:
                i+=1
                
        


        
                    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        