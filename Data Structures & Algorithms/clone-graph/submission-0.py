"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_map = {}
        
        def dfs(n):
            if n in clone_map:
                return clone_map[n]
            
            clone = Node(n.val)
            clone_map[n] = clone

            for neighbor in n.neighbors:
                clone_neighbor = dfs(neighbor)
                clone.neighbors.append(clone_neighbor)
            return clone
        return dfs(node)
                


        