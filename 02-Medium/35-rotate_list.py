# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Make the linked list circular
        tail.next = head
        
        # Step 3: Find the effective rotations needed
        k = k % length
        if k == 0:
            tail.next = None
            return head
            
        # Step 4: Find the new tail (length - k steps from head)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # Step 5: Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head