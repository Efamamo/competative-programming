class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def solve(grid, row, col):
            return (grid[row][col] + grid[row-1][col] + grid[row-1][col-1] + grid[row-1][col+1] + grid[row+1][col] + grid[row+1][col-1] + grid[row+1][col+1])
        currSum = float("-inf")
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                temp = solve(grid, i, j)
                if currSum < temp:
                    currSum = temp
        return currSum

        