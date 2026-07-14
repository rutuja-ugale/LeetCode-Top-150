class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur_line, num_of_letters = [], [], 0
        
        for w in words:
            # Check if adding the new word exceeds maxWidth
            # (len(cur_line) is the number of spaces needed between words)
            if num_of_letters + len(cur_line) + len(w) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    # Use modulo to distribute spaces round-robin to the left slots
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '
                res.append("".join(cur_line))
                cur_line, num_of_letters = [], 0
            
            cur_line.append(w)
            num_of_letters += len(w)
            
        # Handle the last line (left-justified)
        res.append(" ".join(cur_line).ljust(maxWidth))
        return res