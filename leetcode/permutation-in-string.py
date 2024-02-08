class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check=defaultdict(int)
        valid=defaultdict(int)
        l=0
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            check[s1[i]]+=1
            valid[s2[i]]+=1
        if check==valid:
            return True
        for i in range(len(s1),len(s2)):
            valid[s2[i]]+=1

            valid[s2[l]]-=1
            if valid[s2[l]]==0:
                del valid[s2[l]]
            l+=1

            if valid==check:
                return True
        return False
            
            
        
        