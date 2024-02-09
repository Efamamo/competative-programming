class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pre_indices = {}
        pre = [0]*len(nums)
        post_indices = {}
        post = [0]*len(nums)
        pre_vals = {}
        post_vals = {}
        pre_arr = [0]*len(nums)
        post_arr = [0]*len(nums)
        
            
        
        for i in range(len(nums)):
            pre[i] = pre_indices.get(nums[i],0)
            pre_arr[i] = pre_vals.get(nums[i],0)
            pre_vals[nums[i]] = 1 + pre_vals.get(nums[i],0)
            pre_indices[nums[i]] = i + pre_indices.get(nums[i],0)
        for i in range(len(nums)-1,-1,-1):
            post_vals[nums[i]] = 1 + post_vals.get(nums[i],0)
            post_arr[i] = post_vals.get(nums[i],0)
            post[i] = post_indices.get(nums[i],0)
            post_indices[nums[i]] = i + post_indices.get(nums[i],0)
        res = [0]*len(nums)
        print(pre_arr,post_arr)
        for i in range(len(nums)):
            res[i] = abs(pre_arr[i]*i-pre[i]) + abs((post_arr[i]-1)*i-post[i])
        

        
            
        
            
        return res
        