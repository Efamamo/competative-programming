class Solution:
    def maxScore(self, s: str) -> int:
        total=0
        maximum=0
        for i in s:
            total+=int(i)
        right=total
        left=0
        for i in range(len(s)-1):
           
            if s[i]=="0":
                left+=1
                maximum=max(maximum,right+left) 

            else:
                right-=1
                maximum=max(maximum,right+left) 

            print(right,left)
        return maximum
        