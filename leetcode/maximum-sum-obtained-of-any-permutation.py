class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = [0]*(len(nums)+1)
        for request in requests:
            res[request[0]]+=1
            res[request[1]+1]-=1
        for i in range(1,len(res)):
            res[i]+=res[i-1]
            
        res.pop()
        res.sort()
        nums.sort()

        

        tot = 0
        for i in range(len(nums)):
            tot += (res[i]*nums[i])
        
        return tot%(10**9 + 7)

        