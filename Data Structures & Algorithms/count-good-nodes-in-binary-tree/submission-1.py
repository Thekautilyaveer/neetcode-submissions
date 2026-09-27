# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, maxN):
            if not root:
                return 0

            if root.val >= maxN:
                maxN = root.val
                return 1+dfs(root.left, maxN)+dfs(root.right, maxN)
            return 0+dfs(root.left, maxN)+dfs(root.right, maxN)

        return dfs(root, root.val)






        