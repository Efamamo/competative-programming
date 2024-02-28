# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxim_diff = float("-inf")
        def inorder(root,parent):
            nonlocal maxim_diff
            if not root:
                return
            for i in parent:
                maxim_diff = max(maxim_diff,abs(root.val-i))
   
            
            left = inorder(root.left,parent+[root.val])
            right = inorder(root.right,parent + [root.val])
            
        inorder(root,[])
        return maxim_diff
        