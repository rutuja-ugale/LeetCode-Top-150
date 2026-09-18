class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        def backtrack(row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # Place queen
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                # Recurse to next row
                count += backtrack(row + 1)
                
                # Remove queen (backtrack)
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
            return count
        return backtrack(0)