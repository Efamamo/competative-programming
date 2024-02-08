class Solution:
    def minimumSteps(self, s: str) -> int:
        sl = []
        for i in s:
            sl.append(i)
        last_0 = len(sl)
        for i in range(len(sl)-1,-1,-1):
            if sl[i] == "0":
                last_0 = i
                break
        if last_0 == len(sl) or last_0 == 0:
            return 0
        count = 0
        for i in range(len(sl)):
            if sl[i]=="1" and i<last_0:
                sl[i],sl[last_0]=sl[last_0],sl[i]
                count+=(last_0-i)
                last_0-=1
                while s[last_0] == "1":
                    last_0-=1
                
                
        return count
                    

        
        