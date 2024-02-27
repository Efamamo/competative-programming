class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        s = []
        def backtrack(res,next_pointer,total):
            print(res,total,next_pointer)
            if next_pointer>=len(candidates):
                return
            if total == target and res not in s:
                s.append(res[:])
                return
            elif total > target:
                return
    
            res.append(candidates[next_pointer])
            backtrack(res,next_pointer,total+candidates[next_pointer])
            res.pop()
            backtrack(res,next_pointer+1,total)
                
        backtrack([],0,0)
            
        return s