class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if maxDoubles:
                if target % 2 ==0:
                    while maxDoubles and target % 2 == 0:
                        target = target//2
                        res += 1
                        maxDoubles -= 1
                else:
                    target -= 1
                    res += 1
            else:
                res += target-1
                target = 1
        return res
                
           
                