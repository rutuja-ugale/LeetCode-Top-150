# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Create dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to track the current ends of the two partitions
        less = less_dummy
        greater = greater_dummy
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
            
        # Terminate the greater list to avoid cycles
        greater.next = None
        
        # Connect the less list to the start of the greater list
        less.next = greater_dummy.next
        
        return less_dummy.next