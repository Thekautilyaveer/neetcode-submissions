# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxval = 0

        def dfs(root):
            if not root:
                return 0
            leftval, rightval = 0, 0
            if root.left:
                leftval = int(dfs(root.left))
            if root.right:
                rightval = int(dfs(root.right))
            nonlocal maxval
            maxval = max(maxval, (leftval + rightval))
            finalval = 1+ max(leftval, rightval)
            return (finalval)

        return max(int(dfs(root))-1, maxval)
        


            
        