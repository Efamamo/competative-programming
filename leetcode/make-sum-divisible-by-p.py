class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p == 0:
            return 0
        reminder = sum(nums)%p
        prefix = {0:-1}
        min_sub = len(nums)
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            
            if (current - reminder)%p in prefix:
                min_sub = min(min_sub,i-prefix[(current - reminder)%p])
            prefix[current%p] = i
        return min_sub if min_sub < len(nums) else -1


        