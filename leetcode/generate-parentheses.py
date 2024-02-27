class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        par = []
        def backtrack(candidate,opened,closed):
            if opened==closed==n:
                par.append("".join(candidate))
                return
            
            if opened < n:
                candidate.append("(")
                backtrack(candidate,opened+1,closed)
                candidate.pop()
                

            if closed < opened:
                candidate.append(")")
                backtrack(candidate,opened,closed+1)
                candidate.pop()
                
        backtrack([],0,0)
        return par


            

        backtrack([],0,0,0)
      
        res = []
        for i in par:
            if valid(i) and i not in res:
                res.append(i)
        
        return res
        