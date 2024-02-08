class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        total=0
        res=0
        for i in range(len(nums)):
            total+=nums[i]
            mod=total%k
            res+=prefix.get(mod,0)
            prefix[mod]=1+prefix.get(mod,0)
        return res
            

