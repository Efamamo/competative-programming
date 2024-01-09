class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans={"T":0,"F":0}
        max_l=0
        l=0
        for r in range(len(answerKey)):
            ans[answerKey[r]]=1+ans.get(answerKey[r],0)
            if (r-l+1-max(ans.values()))>k:
                ans[answerKey[l]]-=1
                l+=1
            max_l=max(max_l,r-l+1)
        return max_l
            


        