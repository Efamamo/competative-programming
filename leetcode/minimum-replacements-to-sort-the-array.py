class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<last:
                last = nums[i]
            else:
                space = nums[i]//last
                
                if nums[i] % last!=0:
                    res += space
                    last = nums[i]//(space+1)
                   
                else:
                    res += space-1
                    last = nums[i]//space
                
        return res
        