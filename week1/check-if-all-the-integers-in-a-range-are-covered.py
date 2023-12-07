class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cov={x for x in range(left,right+1)}
        for i in ranges:
            for j in range(i[0],i[1]+1):
              cov.discard(j)
             
        return len(cov)==0