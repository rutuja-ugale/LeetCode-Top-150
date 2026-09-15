class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start):
            # If we've reached the end of the array, we have a complete permutation
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Choose: Swap the current element with the start index
                nums[start], nums[i] = nums[i], nums[start]
                
                # Explore: Recurse for the next index
                backtrack(start + 1)
                
                # Un-choose (Backtrack): Undo the swap to restore the array for the next iteration
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return res