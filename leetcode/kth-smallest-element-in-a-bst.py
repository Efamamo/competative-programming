# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = k
        def kth(root):
            nonlocal l
            if not root:
                return []
            left = kth(root.left)
            right = kth(root.right)
            return left + [root.val] + right
        return kth(root)[k-1]

        

        
        
                    
        