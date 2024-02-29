class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(n):
            if n == 0:
                return 1
            return n*fact(n-1)
        def C(n,r):
            t1 = fact(n)
            t2 = fact(r)
            t3 = fact(n-r)
            print(t1,t2,t3)
            return t1//(t2*t3)
       

        res = []
        for i in range(rowIndex+1):
            res.append(C(rowIndex,i))
        return res
        
        