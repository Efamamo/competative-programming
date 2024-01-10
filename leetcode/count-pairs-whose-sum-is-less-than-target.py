class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        count=0
        while l<r:
            if nums[l]+nums[r]<target:
                count+=(r-l)
                print(l,r,count)
                l+=1
            else:
                r-=1
        return count

        