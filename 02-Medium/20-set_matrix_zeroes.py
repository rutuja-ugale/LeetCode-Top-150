class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # Flags to check if the first row or first column originally had zeros
        row_zero = False
        col_zero = False
        
        # Check if any element in the first column is zero
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
                
        # Check if any element in the first row is zero
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break
                
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Fill inner matrix based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Update first column if needed
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
                
        # Update first row if needed
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0