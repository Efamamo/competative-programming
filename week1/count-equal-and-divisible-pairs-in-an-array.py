class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        vals = defaultdict(set)
        count=0
        for i,val in enumerate(nums):
            for j in vals[val]:
                if (i*j)%k==0:
                    count+=1
            vals[val].add(i)
        return count



            


        