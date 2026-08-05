# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast pointer n + 1 steps ahead to maintain a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Remove the target node
        slow.next = slow.next.next
        
        return dummy.next