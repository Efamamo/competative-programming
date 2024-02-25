# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if min(p.val,q.val)<=root.val<=max(q.val,p.val):
            return root
        elif root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
        
        