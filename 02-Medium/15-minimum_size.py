class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            # While the current window sum is >= target, 
            # try to shrink it from the left to find a smaller length
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_length if min_length != float('inf') else 0