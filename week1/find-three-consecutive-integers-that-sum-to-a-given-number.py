class Solution(object):
    def sumOfThree(self, num):
        result=num//3 -1
        results=[]
        if result+result+1+result+2==num:
            results.append(result)
            results.append(result+1)
            results.append(result+2)
        return results
        """
        :type num: int
        :rtype: List[int]
        """
        