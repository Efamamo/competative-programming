class Solution(object):
    def isAnagram(self, s, t):
        arr = [0]*26
        for i in s:
            idx=ord(i)-97
            arr[idx]+=1
        for i in t:
            idx=ord(i)-97
            arr[idx]-=1
        for i in arr:
            if i:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
