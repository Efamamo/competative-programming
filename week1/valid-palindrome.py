class Solution(object):
    def isPalindrome(self, s):
        st=""
        for i in s.lower():
            if i.isalnum():
                st+=i
        i=0
        j=len(st)-1
        while i<=j:
            if st[i]!=st[j]:
                return False
            i+=1
            j-=1
        return True
        """
        :type s: str
        :rtype: bool
        """
        