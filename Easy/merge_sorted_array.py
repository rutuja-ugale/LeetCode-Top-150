class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize three pointers from the back of the arrays
        p1 = m - 1        # Pointer for the last valid element in nums1
        p2 = n - 1        # Pointer for the last element in nums2
        p = m + n - 1     # Pointer for the very last position in nums1
        
        # Compare elements from the back and place the larger one at index p
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # Place nums1 element at the end
                p1 -= 1               # Move nums1 pointer backwards
            else:
                nums1[p] = nums2[p2]  # Place nums2 element at the end
                p2 -= 1               # Move nums2 pointer backwards
            p -= 1                    # Move the main tracking pointer backwards
        
        # If there are any remaining elements left in nums2, copy them over
        # (Leftover elements in nums1 are already in their correct sorted positions)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# ==========================================================
# Driver Code (To test the output on your local machine)

# 1. Input Data
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# 2. Create an instance of the class and call the function
ob = Solution()
ob.merge(nums1, m, nums2, n)

# 3. Print the final modified array
print(nums1)  