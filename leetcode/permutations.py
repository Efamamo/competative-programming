class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(candidate,hashset):

            if len(candidate) == len(nums):
                res.append(candidate[:])
        
            for i in range(len(nums)):
                if nums[i] in hashset:
                    continue
                candidate.append(nums[i])
                hashset.add(nums[i])
                backtrack(candidate,hashset)
                hashset.remove(candidate[-1])
                candidate.pop()

        backtrack([],set())
        return res


        