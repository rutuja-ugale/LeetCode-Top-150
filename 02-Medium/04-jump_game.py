class Solution(object):
    def canJump(self, nums):
        max_reachable = 0
        last_index = len(nums) - 1
        for i, jump in enumerate(nums):
            # if current index is unreachable, we can't go further
            if i > max_reachable:
                return False
            # update the furthest point we can reach
            max_reachable = max(max_reachable, i + jump)
            # optimization: if we already reached the end, return True
            if max_reachable >= last_index:
                return True
        return False