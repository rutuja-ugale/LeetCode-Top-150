class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            j = i
            # Find the end of the consecutive range
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            
            # Format based on whether it's a single number or a range
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))
                
            # Move to the next range start
            i = j + 1
            
        return res