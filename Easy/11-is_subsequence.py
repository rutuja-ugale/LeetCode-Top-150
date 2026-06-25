class Solution(object):
    def isSubsequence(self, s, t):
        # if s is empty, it is always a subsequence
        if not s:
            return True
        i, j == 0, 0
        # traverse t and match characters of s
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                # if we've matched all characters in s
            if i == len(s):
                return True
            j += 1
        return False 