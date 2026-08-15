# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        in_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1
        
        def helper(in_left, in_right):
            # Base case: if there are no elements to construct the subtree
            if in_left > in_right:
                return None
                
            # The current root value is at post_idx; decrement the index for the next recursive call
            val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(val)
            
            # Split inorder traversal into left and right subtrees based on root's index
            idx = in_map[val]
            
            # Build right subtree first because we are moving backwards through postorder
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)