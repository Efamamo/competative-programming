# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def inorder(root):
            nonlocal res
            if not root:
                return 0
            
            if low<=root.val<=high:
                res += root.val
            
            left = inorder(root.left)
            right = inorder(root.right)
            return res
        return inorder(root)
        
        
        