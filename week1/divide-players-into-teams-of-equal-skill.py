class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum=skill[0]+skill[-1]
        total=skill[0]*skill[-1]
        i=1
        j=len(skill)-2
        while i<j:
            if skill[i]+skill[j]==sum:
                total+=skill[i]*skill[j]
            else:
                return -1
            i+=1
            j-=1
   
        return total
        