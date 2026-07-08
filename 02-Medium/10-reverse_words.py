class Solution(object):
    def reverseWords(self, s):
        # 1. split without arguments automatically handles
        # multiple spaces and ignores leading/trailing whitespaces.
        words = s.split()
        # 2. reverse the list of words.
        words.reverse()
        # 3. join the words with a single space.
        return " ".join(words)