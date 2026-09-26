class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        curr_max = 0
        max_sum = nums[0]
        curr_min = 0
        min_sum = nums[0]
        
        for num in nums:
            # Kadane's for maximum subarray sum
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Kadane's for minimum subarray sum
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            
            total_sum += num
            
        # If all numbers are negative, max_sum will be the maximum negative element
        if max_sum < 0:
            return max_sum
            
        return max(max_sum, total_sum - min_sum)