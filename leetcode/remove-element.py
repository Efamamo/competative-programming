class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0

        for i in range(len(nums)):

            if nums[i]==val:
                l=i
                break
        else:
            return len(nums)

        if i==len(nums):
            return len(nums)
        
        for r in range(l+1,len(nums)):
            
            if nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        
        return l
