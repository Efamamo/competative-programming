class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        res = A[0]
        total = A[0]
        for i in range(1,len(A)):
            total+=A[i]
            if total % (i+1) == 0:
                res = max(res,(total//(i+1)))
            else:
                res = max(res,(total//(i+1)+1))
        return res

        

        