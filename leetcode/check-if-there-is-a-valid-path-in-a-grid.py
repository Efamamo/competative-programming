class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [[0,-1],[0,1]],
            2: [[-1,0],[1,0]],
            3: [[0,-1],[1,0]],
            4: [[1,0],[0,1]],
            5: [[0,-1],[-1,0]],
            6: [[-1,0],[0,1]]
            
        }
        def inbound(row,column):
            return 0<= row <len(grid) and 0 <= column < len(grid[0])

        def dfs(visited,row,column,rc,cc):
            
            if(row,column) != (0,0) and [-rc,-cc] not in directions[grid[row][column]]:
                return 
           
            if (row,column) == (len(grid)-1,len(grid[0])-1):
                return True
            visited.add((row,column))
            
            for rc,cc in directions[grid[row][column]]:
                
                new_row = row + rc
                new_col = column + cc
                
               
                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    val = dfs(visited,new_row,new_col,rc,cc)

                    if val:
                        return True
            return False

        return dfs(set(),0,0,0,0)

        