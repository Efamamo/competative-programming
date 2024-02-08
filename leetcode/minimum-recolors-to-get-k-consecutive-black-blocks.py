class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        blacks=0
        min_o=k
        for r in range(len(blocks)):
            print(blocks[l:r+1],blacks)
            if r-l==k:
                if blocks[l]=="B":
                    blacks-=1
                l+=1
            if blocks[r]=="B":
                blacks+=1
                
            min_o=min(min_o,k-blacks)
        return min_o
        