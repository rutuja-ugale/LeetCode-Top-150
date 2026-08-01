from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of our merged list
        dummy = ListNode()
        curr = dummy
        
        # Traverse both lists while nodes are available in both
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Attach any remaining nodes from either list
        curr.next = list1 if list1 else list2
        
        # Return the head of the merged list (skipping the dummy node)
        return dummy.next