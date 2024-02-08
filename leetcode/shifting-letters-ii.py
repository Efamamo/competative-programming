class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0]*len(s)
        for i in shifts:
            if i[2] == 0:
                i[2]=-1
        for i in shifts:
            ans[i[0]]+=i[2]
            if i[1]+1<len(s):
                ans[i[1]+1]-=i[2]
        for j in range(1,len(ans)):
            ans[j] +=ans[j-1]
        res = ""
        for i in range(len(s)):
            val = ord(s[i])+ans[i]
            if val < 97: 
                res += chr(( 122 - (96 - (val))%26))
            elif val > 122:
                res += chr(( 97 + ((val) - 123)%26))
            else:
                res += chr(val)
        return res

