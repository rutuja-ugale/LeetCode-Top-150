# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            # If current node has a duplicate ahead
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the duplicate value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Link prev to the node after the duplicates
                prev.next = curr.next
            else:
                # No duplicate, advance prev pointer
                prev = prev.next
            
            # Move curr forward
            curr = curr.next
            
        return dummy.next