# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        # Calculate left and right heights
        lh, rh = 0, 0
        curr = root
        while curr.left:
            lh += 1
            curr = curr.left
            
        curr = root
        while curr.right:
            rh += 1
            curr = curr.right
            
        # If left and right heights are equal, it's a full binary tree
        if lh == rh:
            return (1 << (lh + 1)) - 1
        
        # Otherwise, recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)