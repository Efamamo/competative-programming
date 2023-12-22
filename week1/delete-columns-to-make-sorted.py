class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted=0
        test=len(strs[0])
        for i in range(test):
            for j in range(len(strs)-1):
                if strs[j][i]>strs[j+1][i]:
                    deleted+=1
                    break
        return deleted


        