class Solution(object):
    def removeDuplicates(self, nums):
        # Base case: If the array is empty, return 0
        if not nums:
            return 0
        
        # 'j' keeps track of the index where the next unique element should be placed
        # The first element (index 0) is always unique, so we start from index 1
        j = 1 
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]  # Move the unique element to index 'j'
                j += 1             # Increment 'j' to point to the next position
                
        # Return 'j', which represents the total count of unique elements
        return j