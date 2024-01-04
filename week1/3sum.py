class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        vals = []
        for idx,target in enumerate(nums) :
            i = idx+1
            j = len(nums) - 1
            if idx>0 and nums[idx-1]==target:
                continue
            while i < j:
                ans=target + nums[i]+ nums[j]
                if ans>0:
                    j -= 1
                elif ans<0:
                    i += 1
                else:
                    vals.append([target, nums[i], nums[j]])
                    i+=1
                    while nums[i]==nums[i-1] and i<j:
                        i+=1
        return vals
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        