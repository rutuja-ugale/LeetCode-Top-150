class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            # Either add the current number to the existing subarray sum,
            # or start a fresh subarray from the current number.
            current_sum = max(num, current_sum + num)
            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum