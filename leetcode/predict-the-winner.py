class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def pre(l,r):
            if l > r:
                return 0
            left = nums[l]-pre(l+1,r)
            right = nums[r]-pre(l,r-1)
            return max(left,right)
        return pre(0,len(nums)-1)>=0
               
          
           
       
        
        
        