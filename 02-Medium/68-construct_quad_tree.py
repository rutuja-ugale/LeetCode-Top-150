# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def dfs(n, r, c):
            # Check if all values in the current subgrid are the same
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != grid[r][c]:
                        all_same = False
                        break
                if not all_same:
                    break
            
            # If all values are uniform, return a leaf node
            if all_same:
                return Node(val=grid[r][c] == 1, isLeaf=True, 
                            topLeft=None, topRight=None, 
                            bottomLeft=None, bottomRight=None)
            
            # Otherwise, divide into 4 quadrants
            half = n // 2
            top_left = dfs(half, r, c)
            top_right = dfs(half, r, c + half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r + half, c + half)
            
            # Return an internal node with the four children
            return Node(val=True, isLeaf=False, 
                        topLeft=top_left, topRight=top_right, 
                        bottomLeft=bottom_left, bottomRight=bottom_right)

        return dfs(len(grid), 0, 0)