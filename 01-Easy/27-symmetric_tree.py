# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        def isMirror(t1, t2):
            # If both nodes are None, they match
            if not t1 and not t2:
                return True
            # If only one of them is None, they don't match
            if not t1 or not t2:
                return False
            
            # Check current values and recursively check outer and inner pairs
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            
        return isMirror(root.left, root.right)