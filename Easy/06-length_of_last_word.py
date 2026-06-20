class Solution(object):
    def lengthOfLastWord(self, s):
        # Remove trailing spaces
        s = s.rstrip()
        # Split the string by spaces and take the last element
        # This handles multiple spaces between words as well
        words = s.split(' ')
        return len(words[-1])