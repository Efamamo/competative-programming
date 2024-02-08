class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique=set()
        l=total=max_res=0
        for r in range(len(nums)):
            total+=nums[r]
            while nums[r] in unique:
                unique.remove(nums[l])
                total-=nums[l]
                l+=1
            unique.add(nums[r])
            max_res=max(max_res,total)
        return max_res
            

        