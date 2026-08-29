class Solution(object):
    def getMinimumDifference(self, root):
        """:type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_diff = float('inf')
        self.prev_val = None
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            
            # Traverse right subtree
            inorder(node.right)
            
        inorder(root)
        return self.min_diff