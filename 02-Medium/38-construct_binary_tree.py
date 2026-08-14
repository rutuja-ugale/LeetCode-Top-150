# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

  def buildTree(self, preorder, inorder):
    """:type preorder: List[int]

    :type inorder: List[int]
    :rtype: Optional[TreeNode]
    """
    # Map values to their indices in the inorder traversal for O(1) lookup
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    self.preorder_idx = 0

    def helper(left, right):
      # Base case: if there are no elements to construct the subtree
      if left > right:
        return None

      # Get the current root value from preorder and advance the index
      root_val = preorder[self.preorder_idx]
      self.preorder_idx += 1
      root = TreeNode(root_val)

      # Split inorder traversal into left and right subtrees using the hash map
      idx = inorder_map[root_val]

      # Recursively build left and right subtrees
      root.left = helper(left, idx - 1)
      root.right = helper(idx + 1, right)

      return root

    return helper(0, len(inorder) - 1)