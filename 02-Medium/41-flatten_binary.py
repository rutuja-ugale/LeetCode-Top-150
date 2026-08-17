# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Rewire: attach current's right subtree to the right of the predecessor
                prev.right = curr.right
                
                # Move left subtree to the right and clear left
                curr.right = curr.left
                curr.left = None
                
            # Move to the next node
            curr = curr.right