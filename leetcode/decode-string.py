class Solution:
    def decodeString(self, s: str) -> str:
        result=[]
        for i in range(len(s)):
            if s[i]!="]":
                result.append(s[i])
            else:
                sub=""
                while result[-1]!="[":
                    sub = result.pop()+sub
                result.pop()
                k=""
                while result and result[-1].isdigit():
                    k=result.pop()+k
                result.append(int(k)*sub)
        return "".join(result)



                

                
                
                
                    
                    

        