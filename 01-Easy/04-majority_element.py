class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            # If count is 0, we pick a new candidate
            if count == 0:
                candidate = num

            # Increment count if it matches the candidate, decrement otherwise
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    