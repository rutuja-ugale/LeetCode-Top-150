# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Recursive calls for left and right subtrees. 
            # If a path sum is negative, we can ignore it by taking max(0, sum).
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))
            
            # Price of a path starting at this node and turning through both children
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max sum of a path extending upwards to the parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return self.max_sum