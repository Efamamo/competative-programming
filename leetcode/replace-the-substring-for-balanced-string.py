class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        valid = len(s)//4

        for i in count:
            if count[i] != valid:
                break
        else:
            return 0

        def compareDicionary(target,current):
            
            for i in target:
                if i in current and current[i]<target[i]:
                    return False
                if i not in current:
                    return False
            return True
        
        target = {}

        for i in count:
            if count[i]>valid:
                target[i] = count[i]-valid
        
        l = 0
        min_window = len(s)

        current = {}
        
        for r in range(len(s)):
            current[s[r]] = 1 + current.get(s[r],0)
            while compareDicionary(target,current): 
                min_window = min(min_window,r-l+1)
                current[s[l]]-=1
                l+=1
            

        return min_window



            
        
        
    


        