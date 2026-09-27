# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        n = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n.append(cur.val)
            cur = cur.right
        return n[k-1]








            
            