"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
            
        vals = {}

        def clone(node, vals):
            if node in vals:
                return vals[node]

            new_node = Node(node.val, [])
            vals[node] = new_node
            
            for n in node.neighbors:
                new_node.neighbors.append(clone(n,vals))

            return new_node

        return clone(node,vals)


        

        
        