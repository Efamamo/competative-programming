class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts={0:1}
        l=0
        total,count=0,0
        for r in range(len(nums)):
            total+=nums[r]
            
            count+=counts.get(total-k,0)
            counts[total]=1+counts.get(total,0)
        return count

        