class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        l = 0
        arrows = 0
        ranges = points[0]
        for r in range(1,len(points)):
            if points[r][0]<= ranges[1]:
                ranges = [max(ranges[0],points[r][0]),min(ranges[1],points[r][1])]
            else:
                arrows += 1
                ranges = points[r]
        return arrows + 1




            
        
        