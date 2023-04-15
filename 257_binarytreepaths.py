# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        s=""
        def traversal(root,s,res):
            if root:
                s+=str(root.val)+"->"
                if root.left==None and root.right==None:
                    res.append(s[:-2])
                else:
                    traversal(root.right,s,res)
                    traversal(root.left,s,res)
        traversal(root,s,res)
        return res