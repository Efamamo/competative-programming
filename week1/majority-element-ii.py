class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=r=0
        test=len(nums)//3
        changed=0
        while r<len(nums):
            if nums[r]!=nums[l]:
                if r-l>test:
                    nums[changed]=nums[l]
                    changed+=1
                l=r
            r+=1
        if r-l>test:
            nums[changed]=nums[l]
            changed+=1
        return nums[:changed]
            

        