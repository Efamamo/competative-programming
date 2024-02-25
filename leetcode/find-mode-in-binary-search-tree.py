# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        arr = inorder(root)
        count = Counter(arr)
        val = max(count.values())
        res = []
        for i in count:
            if count[i] == val:
                res.append(i)
        return res
        
    