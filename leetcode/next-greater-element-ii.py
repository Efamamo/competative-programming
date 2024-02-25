class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        d = {}
        
        for i in range(2*len(nums)):
            while st and nums[st[-1]] < nums[i%len(nums)]:
                d[st.pop()] = nums[i%len(nums)]
            
            st.append(i%len(nums))
       
        for i in range(len(nums)):
            if i in d:
                nums[i] = d[i]
            else:
                nums[i] = -1
        return nums

        