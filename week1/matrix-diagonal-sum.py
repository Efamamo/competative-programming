class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j==len(mat)-1:
                    total+=mat[i][j]
                    mat[i][j]=0
        return total
        