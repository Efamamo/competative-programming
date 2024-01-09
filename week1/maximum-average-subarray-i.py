class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avr=float("-inf")
        r=0
        l=0
        total=0
        while r<len(nums):
            total+=nums[r]
            if r-l+1==k:
                max_avr=max(max_avr,total/k)
                total-=nums[l]
                l+=1
            r+=1
        return max_avr
        