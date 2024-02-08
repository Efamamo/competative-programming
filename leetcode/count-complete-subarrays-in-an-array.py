class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = set(nums)
        distnict = len(count)

        l = 0
        count = 0
        sub = {}
        for r in range(len(nums)):
            while len(sub) == distnict:
               
                count+=(len(nums)-r+1)
                print(sub,count)
                sub[nums[l]]-=1
                if sub[nums[l]] == 0:
                    del sub[nums[l]]
                l+=1
            sub[nums[r]] = 1 + sub.get(nums[r],0)
        while len(sub) == distnict and l<len(nums):
            count+=1
            sub[nums[l]]-=1
            if sub[nums[l]] == 0:
                del sub[nums[l]]
            l+=1
        return count
        