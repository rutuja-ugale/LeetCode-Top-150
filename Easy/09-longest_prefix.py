class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return " "
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        # Compare the prefix with every other string in the list
        for i in range(1, len(strs)):
            # while the current string doesn't start with the prefix
            while not strs[i].startswith(prefix):
                # shorten the prefix by removing the last character
                prefix = prefix[:-1]
                # if the prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        return prefix