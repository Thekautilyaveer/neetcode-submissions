# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        res1 = []
        res2 = []

        def traverse(root, res):
            if not root:
                res.append('#')
                return
            res.append(root.val)
            traverse(root.left, res)
            traverse(root.right, res)

            return res


        l1 = traverse(root, res1)
        l2 = traverse(subRoot, res2)

        first = 0
        sec = len(l2)
        while sec <= len(l1):
            if l1[first:sec] == l2:
                return True
            else:
                first +=1 
                sec +=1
        return False
    
    
        