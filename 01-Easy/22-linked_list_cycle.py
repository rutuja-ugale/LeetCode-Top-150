class Solution(object):
    def hasCycle(self, head):
        """:type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if slow == fast:          # Cycle detected
                return True
                
        return False                  # Reached the end, no cycle