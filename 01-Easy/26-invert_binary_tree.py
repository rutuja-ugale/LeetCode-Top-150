class Solution(object):
    def invertTree(self, root):
        """:type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the tree is empty, return None
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root