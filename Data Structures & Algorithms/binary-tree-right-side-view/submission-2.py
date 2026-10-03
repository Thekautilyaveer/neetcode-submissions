# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []  
        result = []
        if not root:
            return []
        node = root
        q.append(node)
        while q:
            lst = []
            for i in range(len(q)): 
                temp = q.popleft()
                lst.append(temp.val) 
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right) 
                
            res.append(lst) 


        for val in res:
            result.append(val[-1])
        return result

