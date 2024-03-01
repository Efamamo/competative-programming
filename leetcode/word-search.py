class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def backtrack(current,r,c):
            
            
            if current == len(word):
                return True
           
            
            if r >= len(board) or r < 0 or c >=len(board[0]) or c<0 or (r,c) in path or word[current]!=board[r][c] :
                return False
         
            
            path.add((r,c))
            res = (backtrack(current+1,r+1,c) 
                    or backtrack(current+1,r-1,c) 
                    or backtrack(current+1,r,c+1) 
                    or backtrack(current+1,r,c-1))
            path.remove((r,c))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(0,i,j):
                    return True
        return False
     

        