class Solution(object):
    def removeDuplicates(self, nums):
        # if the arr has 2 or fewer elements, no duplicates can exceed the limit
        if len(nums) <= 2:
            return len(nums)
        # 'k' acts as the write pointer
        # we start at 2 because the first two elements are always allowed
        k = 2
        # iterate through the rest of the array
        for i in range(2, len(nums)):
            # if current element is different from the one two spots behind our write pointer,
            # it means this is either the first or second occurance of this number
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k