class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        pathx=0
        pathy=0
        path=0
        for i in range(len(points)-1):
            pathx=(abs(points[i+1][0]-points[i][0]))
            pathy=(abs(points[i+1][1]-points[i][1]))
            path+=max(pathx,pathy)
        return path
            

                

        