# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxi_sum = 0
        def max_sum(root):
            nonlocal maxi_sum
            if root:
                if not root.left and not root.right:
                    maxi_sum = max(maxi_sum,root.val)
                    return (root.val,True,root.val,root.val)
            
                lsum,lbst,lmax,lmin = max_sum(root.left)
                rsum,rbst,rmax,rmin  = max_sum(root.right)
                

                if lmax < root.val < rmin and rbst and lbst:
                    maxi_sum = max(maxi_sum,root.val + lsum+rsum)
                    return (root.val+lsum+rsum,True,max(rmax,root.val),min(lmin,root.val))
                else:   
                    return (0,False,root.val,root.val)
            else:
                return (0,True,float("-inf"),float("inf"))
  
        max_sum(root)
        return maxi_sum
            

        