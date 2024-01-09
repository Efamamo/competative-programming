class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sum = 0
        minimum = math.inf
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minimum = min(minimum, r-l+1)
                sum -= nums[l]
                l += 1

        return minimum if minimum != math.inf else 0
        