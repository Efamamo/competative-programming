class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=0
        r=len(x)-1
        while r>=l:
            if x[r]!=x[l]:
                return False
            r-=1
            l+=1
        return True
        