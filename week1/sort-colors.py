class Solution(object):
    def sortColors(self, nums):
        count_0=0
        count_1=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_0+=1
            elif nums[i]==1:
                count_1+=1
        for i in range(len(nums)):
            if i<count_0:
                nums[i]=0
            elif count_0 <=i< count_0+count_1:
                nums[i]=1
            else:
                nums[i]=2
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """