class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_h = min(height[left], height[right])
            current_w = right - left
            max_area = max(max_area, current_h * current_w)
            
            # Move the shorter pointer inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area