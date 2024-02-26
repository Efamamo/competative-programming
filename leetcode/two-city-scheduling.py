class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in costs:
            diff.append(i[0]-i[1])
        res = []
        for i in range(len(diff)):
            res.append([diff[i],costs[i]])
        res.sort()
        i = 0
        cost = 0
        while i<len(costs)//2:
            cost+=res[i][1][0]
            i+=1
        while i<len(costs):
            cost+=res[i][1][1]
            i+=1
        return cost

        
        