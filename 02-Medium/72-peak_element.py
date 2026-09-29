class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If the element to the right is greater, a peak must be on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak must be on the left side (including mid)
            else:
                right = mid
                
        return left