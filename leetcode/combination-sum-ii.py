class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(candidate,current,pointer):
            print(candidate)
            if current == target:
                res.append(candidate[:])
                return
            if current > target:
                return
           
            prev = -1
            for i in range(pointer,len(candidates)):
                if prev == candidates[i]:
                    continue
                candidate.append(candidates[i])
                backtrack(candidate,current+candidates[i],i+1)
                candidate.pop()
                prev = candidates[i]
      
        backtrack([],0,0)
        return res
        