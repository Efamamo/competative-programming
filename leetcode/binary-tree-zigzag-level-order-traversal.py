# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        def zig(root,j):
            if not root:
                return 
            
            res[j].append(root.val)
            left = zig(root.left,j+1)
            right = zig(root.right,j+1)
           
        zig(root,0)
        ans = [i for i in res.values()]
        for i in range(len(ans)):
            if i%2 != 0:
                ans[i].reverse()
        return ans

        