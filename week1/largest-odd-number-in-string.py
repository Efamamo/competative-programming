class Solution:
    def largestOddNumber(self, num: str) -> str:
        res=""
        for i in range(len(num)):
            if int(num[i])%2!=0:
                res=num[0:i+1]
        return res
        