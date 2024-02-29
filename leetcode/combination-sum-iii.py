class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(candidate,pos):
            print(candidate)
            if sum(candidate) == n and len(candidate)==k:
                res.append(candidate[:])
                return
            if sum(candidate)>n:
                return
            if pos > n:
                return
            if pos<=9:
                candidate.append(pos)
                backtrack(candidate,pos+1)
                candidate.pop()
                backtrack(candidate,pos+1)

        backtrack([],1)
        return res

            

        