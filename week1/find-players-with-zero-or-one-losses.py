class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost={}
        res=[set(),set()]
        for i in matches:
            lost[i[1]]=1+ lost.get(i[1],0)
        for i in matches:
            if i[0] not in lost:
                res[0].add(i[0])
            if lost[i[1]] ==1:
                res[1].add(i[1])
        res[1]=list(res[1])
        res[0]=list(res[0])
        res[0].sort()
        res[1].sort()
        return res
        
        



        