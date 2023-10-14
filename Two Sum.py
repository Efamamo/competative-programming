class Solution(object):
    def twoSum(self, nums, target):
        List=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    List.append(i)
                    List.append(j)
                    return List

    
        
