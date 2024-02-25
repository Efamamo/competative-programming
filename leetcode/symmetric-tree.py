# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def inorder(root,flag):
            if flag:
                if not root:
                    return []
                l =     inorder(root.left,flag)
                r =     inorder(root.right,flag)
                if not l and r:
                    return [root.val] + ["null"]+ r
                elif not r and l:
                    return [root.val] + l + ["null"]
                return [root.val] + l + r
            else:
                if not root:
                    return []
                l = inorder(root.left,flag)
                r = inorder(root.right,flag)
                if not l and r:
                    return [root.val] + r + ["null"]
                elif not r and l:
                    return [root.val] + ["null"] + l
                return [root.val]+ r + l
        return inorder(root.left,True)== inorder(root.right,False)
        
          

        
        

      

        