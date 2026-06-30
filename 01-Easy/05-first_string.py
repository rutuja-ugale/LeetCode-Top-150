class Solution(object):
    def strStr(self, haystack, needle):
        # Edge case: If needle is empty (though constraints say length >= 1)
        if not needle:
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        # Slide a window of size n_len across haystack
        # We only need to loop up to (h_len - n_len + 1)
        for i in range(h_len - n_len + 1):
            # Check if the substring matches the needle
            if haystack[i : i + n_len] == needle:
                return i
            # If the needle is never found, return -1
        return -1