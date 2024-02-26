# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        def mat(root,i,j):
            if not root:
                return
            if (j,i) in res:
                res[(j,i)].append(root.val)
            else:
                res[(j,i)] = [root.val]
            
            left = mat(root.left,i+1,j-1)
            right = mat(root.right,i+1,j+1)
        mat(root,0,0)

        output = []
        for i in res:
            output.append([i,res[i]])
        output.sort()
        for i in output:
            i[1] = sorted(i[1])
        res = defaultdict(list)
        for i in output:
            res[i[0][0]].extend(i[1])
        ans = []
        for i in res:
            ans.append(res[i])
        return ans
        

        
        
        
      
        

        