class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        r=""
        i=len(s)-1
        while i>=0:
            new=[]
            while s[i]!=" " and i>=0:
                new.append(s[i])
                i-=1
            for k in range(len(new)-1,-1,-1):
                r+=new[k]
            while s[i]==" ":
                i-=1
                
            r+=" "
        return r.strip()
            


        