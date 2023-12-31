class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for i in range(len(points)):
            points[i]=(points[i],(points[i][0]**2 + points[i][1]**2)**0.5)
        points.sort(key= lambda x: x[1])
        for i in range(k):
            res.append(points[i][0])
        return res
        