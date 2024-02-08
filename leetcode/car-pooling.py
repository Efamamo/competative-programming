class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end = 0
        for trip in trips:
            end = max(end,trip[2])
        res = [0]*(end+2)
        for trip in trips:
            res[trip[1]]+=trip[0]
            res[trip[2]]-=trip[0]
        for i in range(2,len(res)):
            res[i]+=res[i-1]
        for i in res:
            if i>capacity:
                return False
        return True

        