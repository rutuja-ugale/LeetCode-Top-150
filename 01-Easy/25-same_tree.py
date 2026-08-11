class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # If both nodes are None, the trees are structurally identical up to this point
        if not p and not q:
            return True
        # If one node is None or their values do not match, they are not the same
        if not p or not q:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val