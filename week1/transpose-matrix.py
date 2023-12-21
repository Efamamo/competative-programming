class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        test=len(matrix[0])
        result=[]
        for i in range(test):
            for j in matrix:
                result.append(j[i])
        arr=[]
        k=0
        while k<len(result):
            val=[]
            for i in range(len(matrix)):
                val.append(result[k])
                k+=1
            arr.append(val)
        return arr

        