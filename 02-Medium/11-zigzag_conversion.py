class Solution(object):
    def convert(self, s, numRows):
        # Edge case: If 1 row or string length is shorter than rows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to store strings for each row
        rows = [''] * numRows
        current_row = 0
        step = 1
        
        for char in s:
            rows[current_row] += char
            
            # If at the top row, go down. If at bottom, go up.
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            
            current_row += step
            
        # Join all rows to get the final result
        return ''.join(rows)