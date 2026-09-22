# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using the slow & fast pointer technique
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Cut the list into two halves
        prev.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        # Attach the remaining nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2
            
        return dummy.next