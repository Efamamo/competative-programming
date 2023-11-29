class Solution(object):
    def checkPowersOfThree(self, n):
        while n>1:
            if n%3==0:
                n//=3
            elif n%3==1:
                n-=1
            else:
                return False
        return True
            
            
        """
        :type n: int
        :rtype: bool
        """
        