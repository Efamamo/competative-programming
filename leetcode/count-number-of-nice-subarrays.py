class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        map={0:1}
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        current_sum=0
        count=0
        for r in range(len(nums)):
            current_sum+=nums[r]
            diff=current_sum-k

            count+=map.get(diff,0)
            map[current_sum]=1+map.get(current_sum,0)
        return count
