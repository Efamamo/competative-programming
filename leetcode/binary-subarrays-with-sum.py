class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = {0:1}
        current,output = 0,0
        for i in nums:
            current += i
            if current - goal in counter:
                output += counter[current-goal]
            counter[current] = 1 + counter.get(current,0)
        return output

