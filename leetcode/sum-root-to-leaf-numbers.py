# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def mySum(root,val):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res += int(val+str(root.val))
            left = mySum(root.left,val+str(root.val))
            right = mySum(root.right,val+str(root.val))
               
        mySum(root,"")
        return res
        
        