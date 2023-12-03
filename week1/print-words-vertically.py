class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr=s.split(" ")
        word=max(arr,key=len)
        result=[]
        for i in range(len(word)):
            val=""
            for j in arr:
                if i<len(j):
                    val+=j[i]
                else:
                    val+=" "
            result.append(val.rstrip())
        return result
            





        