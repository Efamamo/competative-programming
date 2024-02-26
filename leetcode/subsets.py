class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        def backtrack(candidate,next_pointer):
            if next_pointer > len(nums):
                return
            
            s.append(candidate[:])

            for i in range(next_pointer,len(nums)):
                candidate.append(nums[i])
                backtrack(candidate,i+1)
                candidate.pop()

        backtrack([],0)
        return s
        