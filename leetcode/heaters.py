class Solution(object):
    def findRadius(self, houses, heaters):
        min_res = 0
        houses.sort()
        heaters.sort()
        for i in houses:
            l,r = 0,len(heaters)
            while l < r:
                m = (l+r)//2
                if heaters[m] <= i:
                    l = m+1
                else:
                    r = m
            if l == len(heaters):
                min_res = max(min_res,abs(heaters[l-1]-i)) 
            elif l == 0:
                min_res = max(min_res,abs(heaters[l]-i))
            else:
                min_res = max(min_res,min(abs(heaters[l]-i),abs(heaters[l-1]-i)))


        return min_res
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        