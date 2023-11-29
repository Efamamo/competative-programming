class Solution(object):
    def smallestEvenMultiple(self, n):
        i=n
        while i%2!=0 or i%n!=0:
            i+=1
        return i
        

        """
        :type n: int
        :rtype: int
        """
        