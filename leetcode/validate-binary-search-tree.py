# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def minimum(root,flag):
            if flag:
                if not root.left:
                    return root.val
                return minimum(root.left,flag)
            else:
                if not root.right:
                    return root.val
                return minimum(root.right,flag)
        if not root:
            return True
        
        left = float("-inf") if not root.left else minimum(root.left,False)
        right = float("inf") if not root.right else minimum(root.right,True)
        
        if not(left<root.val<right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)