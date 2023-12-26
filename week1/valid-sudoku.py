class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j]!=".":
                    s.add(board[i][j])
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i]!=".":
                    s.add(board[j][i])
        res=defaultdict(list)
        for i in range(9):
            for j in range(9):
                res[i//3,j//3].append(board[i][j])
        print(res)
        for i in res:
            s=set()
            for j in range(len(res[i])):
                if res[i][j]!="." and res[i][j] in s:
                    return False
                s.add(res[i][j])
        # for i in res:
        #     s=set()
        #     for j in range(9):
        #         print(res[i])
        #         if res[i][j]!="." and res[i][j] in s:
        #                 return False
               
        #         s.add(board[i][j])

        return True
                
        