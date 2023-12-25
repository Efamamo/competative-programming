class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal=defaultdict(list)
        result=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                diagonal[i+j].append(mat[i][j])
        for i in diagonal:
           
            if i%2!=0:
                for j in range(len(diagonal[i])):
                    result.append(diagonal[i][j])
            else:
                for j in range(len(diagonal[i])-1,-1,-1):
                    result.append(diagonal[i][j])
        return result


        


                    