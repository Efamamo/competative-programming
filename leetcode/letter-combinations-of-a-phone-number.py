class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        if not digits:
            return []
        def backtrack(candidate,pointer):
            if len(candidate) == len(digits):
                res.append("".join(candidate))
                return
            arr = []
            for i in digits:
                arr.append(alpha[int(i)-2])
            if pointer >= len(arr):
                return
            for i in range(len(arr[pointer])):
                candidate.append(arr[pointer][i])
                backtrack(candidate,pointer+1)
                candidate.pop()
                backtrack(candidate,pointer+1)
        backtrack([],0)
        return res
        
