"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # HashMap to store mapping from original node to its clone
        old_to_new = {}
        
        def dfs(curr):
            # If the node is already cloned, return the clone from the hash map
            if curr in old_to_new:
                return old_to_new[curr]
            
            # Create a clone for the current node
            copy = Node(curr.val)
            old_to_new[curr] = copy
            
            # Recursively clone all neighbors and add them to the copy's neighbors list
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node)