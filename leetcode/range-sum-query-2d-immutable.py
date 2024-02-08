class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i==0 and j ==0:
                    continue
                elif i==0:
                    self.matrix[i][j]=self.matrix[i][j-1]+self.matrix[i][j]
                elif j==0:
                    self.matrix[i][j]=self.matrix[i-1][j]+self.matrix[i][j]
                else:
                    self.matrix[i][j] = self.matrix[i-1][j]+self.matrix[i][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]
        for i in self.matrix:
            i.append(0)
        s = [0]*len(self.matrix[0])
        self.matrix.append(s)

        
        print(self.matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2]-self.matrix[row1-1][col2]-self.matrix[row2][col1-1]+ self.matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)