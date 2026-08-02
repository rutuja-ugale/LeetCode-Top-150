from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Create a dummy node to easily handle edge cases (like left = 1)
        dummy = ListNode(0, head)
        prev = dummy

        # 1. Move 'prev' to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # 2. Reverse the sublist from 'left' to 'right' in-place
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        # 3. Return the updated head of the list
        return dummy.next