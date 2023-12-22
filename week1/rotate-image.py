class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix[i])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            matrix[i].reverse()
        return matrix


        """
        Do not return anything, modify matrix in-place instead.
        """
        