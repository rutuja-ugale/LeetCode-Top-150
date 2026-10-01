class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # Search left for the first occurrence
                    else:
                        left = mid + 1   # Search right for the last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        first = find_bound(is_first=True)
        last = find_bound(is_first=False)
        
        return [first, last]