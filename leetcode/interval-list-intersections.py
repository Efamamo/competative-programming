class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            if firstList[i][1]>secondList[j][0]:
                st=max(firstList[i][0],secondList[j][0])
                end=min(firstList[i][1],secondList[j][1])
                if end>=st:
                    res.append([st,end])
            elif firstList[i][0]<secondList[j][1]:
                st=max(firstList[i][0],secondList[j][0])
                end=min(firstList[i][1],secondList[j][1])
                if end>=st:
                    res.append([st,end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return res

        