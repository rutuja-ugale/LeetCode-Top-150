class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Calculate sub-box index
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check for duplicates
                if (val in rows[i] or 
                    val in cols[j] or 
                    val in boxes[box_index]):
                    return False
                
                # Add value to sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
                
        return True