class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_len=0
        while nums_set:
            num=nums_set.pop()
            next_val=num+1
            while next_val in nums_set:
                nums_set.remove(next_val)
                next_val+=1
            prev_val=num-1
            while prev_val in nums_set:
                nums_set.remove(prev_val)
                prev_val-=1
            max_len=max(max_len,(next_val-prev_val-1))
        return max_len

