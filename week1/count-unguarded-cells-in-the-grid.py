class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls=set((i,j) for i,j in walls)
        guards=set((i,j) for i,j in guards)
        res=set()
        for guard in guards:
            i,j=guard
            while i<m:
                if i==guard[0]:
                    i+=1
                    continue
                elif (i,j) in guards or (i,j) in walls:
                    break
                res.add((i,j)) 
                i+=1
                 
            i=guard[0]
            while i>=0:
                if i==guard[0]:
                    i-=1
                    continue
                elif (i,j) in guards or (i,j) in walls:
                    break
                res.add((i,j)) 
                i-=1
                
                
            i=guard[0]
            while j<n:
                if j==guard[1]:
                    j+=1
                    continue
                elif (i,j) in guards or (i,j) in walls:
                    break
                res.add((i,j)) 
                j+=1
                
                
            j=guard[1]
            while j>=0:
                if j==guard[1]:
                    j-=1
                    continue
                elif (i,j) in guards or (i,j) in walls:
                    break
                res.add((i,j)) 
                j-=1
                
        print(res) 
                
        return m*n-len(guards)-len(walls)-len(res)
        




            




       


                