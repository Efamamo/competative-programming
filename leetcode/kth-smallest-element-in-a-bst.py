# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 1
        val = None
        def kth(root):
            nonlocal counter
            nonlocal val
            if not root:
                return 0
            left = kth(root.left)
            if counter == k:
                val = root.val
            counter += 1
            right = kth(root.right)
        
        kth(root)
        return val


        

        
        
                    
        