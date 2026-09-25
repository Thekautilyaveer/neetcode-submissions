# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        def traverse_inorder(root, res):

            
            if not root:
                res.append(None)
                return 0
            res.append(root.val)
            traverse_inorder(root.left, res)
            
            traverse_inorder(root.right, res)
            return res
        return(traverse_inorder(p, res1) == traverse_inorder(q, res2))

    
        






            
        