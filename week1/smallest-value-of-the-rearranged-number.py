class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>=0:
            k=str(num)
            res=[]
            for i in k:
                res.append(i)
            res.sort()
            if res[0]=="0":
                for i in range(len(res)):
                    if res[i]!="0":
                        res[0],res[i]=res[i],res[0]
                        break
                    
            return int("".join(res))
        else:
            k=str(num)
            res=[]
            for i in range(1,len(k)):
                res.append(k[i])
            res.sort(reverse=True)
            if res[0]=="0":
                for i in range(len(res)):
                    if res[i]!="0":
                        res[0],res[i]=res[i],res[0]
                        break
                    
            return -int("".join(res))