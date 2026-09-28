"""
# Definition for a Node.
class Node:, assert_type
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        o_to_n = {}
        stk = []
        stk.append(node)
        visited = []

        while stk:
            newnode = stk.pop()
            if newnode not in visited:
                visited.append(newnode)
                o_to_n[newnode] = Node(newnode.val)
                for i in newnode.neighbors:
                    stk.append(i)

        for old, new in o_to_n.items():
            for i in old.neighbors:
                new.neighbors.append(o_to_n[i])

        return o_to_n[node]