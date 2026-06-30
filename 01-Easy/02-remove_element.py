class Solution(object):
    def removeElement(self, nums, val):
        # Pointer to track the position of elements not equal to val
        k = 0
        # Iterate through every element in the array
        for i in range(len(nums)):
            # If the current element is not the value we want to remove
            if nums[i] != val:
                # Place it at the index pointed to by k
                nums[k] = nums[i]
                # Move the pointer k to the next position
                k += 1
        # Return the number of elements that are not equal to val
        return k