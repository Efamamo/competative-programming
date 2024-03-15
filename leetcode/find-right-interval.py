class Solution(object):
    def findRightInterval(self, intervals):
        arr = []
        for i in intervals:
            arr.append(i[0])
        for i,e in enumerate(arr):
            arr[i] = (e,i)
        arr.sort()
        ans = []
        for i in range(len(intervals)):
            l, r = 0, len(arr)-1
            while l < r:
                m = (l+r)//2
              
                if arr[m][0] < intervals[i][1]:
                    l = m+1
                else:
                    r = m
                
            if arr[l][0] >= intervals[i][1]:
                ans.append(arr[l][1])
            else:
                ans.append(-1)
        return ans

        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        