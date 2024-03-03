# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = [(0, root)]
        ans = 0
        while q:
            n = len(q)
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)
                if node.left:
                    q.append((2*idx+1 , node.left))
                if node.right:
                    q.append((2*idx+2 , node.right))
            
            ans = max(ans, max(nodes)-min(nodes)+1)
        return ans