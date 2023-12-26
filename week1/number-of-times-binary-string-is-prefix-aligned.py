class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        running=0
        ind_sum=0
        count=0
        for i,e in enumerate(flips):
            running+=e
            ind_sum+=i+1
            if running==ind_sum:
                count+=1
        return count


        