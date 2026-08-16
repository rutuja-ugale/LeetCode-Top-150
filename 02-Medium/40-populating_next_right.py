# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):

  def connect(self, root):
    """:type root: Node

    :rtype: Node
    """
    if not root:
      return None

    # 'head' points to the start of the current level being processed
    head = root

    while head:
      # Dummy node serves as the starting point for the next level's linked list
      dummy = Node(0)
      tail = dummy

      # Traverse the current level using the 'next' pointers
      curr = head
      while curr:
        if curr.left:
          tail.next = curr.left
          tail = tail.next
        if curr.right:
          tail.next = curr.right
          tail = tail.next
        curr = curr.next

      # Move to the next level
      head = dummy.next

    return root