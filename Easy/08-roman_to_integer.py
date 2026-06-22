class Solution(object):
    def romanToInt(self, s):
        # Map of Roman symbols to their integer values
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            # If this is not the last symbol and current value < next value,
            # subtract the current value.
            if i < n - 1 and values[s[i]]< values [s[i]]:
                total -= [s[i]]
            else:
                # Otherwise, add the current value.
                total += [s[i]]
        return total