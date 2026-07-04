class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0
        # we don't need to jump from the last element, so iterate to n - 1
        for i in range(len(nums) - 1):
            # update the furthest point reachable from current or previous positions
            farthest = max(farthest, i + nums[i])
            # if we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                # optimization: if we can already reach the end, break early
                if current_end >= len(nums) - 1:
                    break
        return jumps