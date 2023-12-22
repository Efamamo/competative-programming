class Solution(object):
    def reverseString(self, s):
        i=0
        j=len(s)-1
        while j>i:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s
        
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """