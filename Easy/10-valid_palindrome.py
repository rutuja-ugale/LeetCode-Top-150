class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            # skip non-alphanumeric characters from the left
            if not s[left].islnum():
                left += 1
            # skip non-alphanumeric characters from the right
            elif not s[right].islnum():
                right -= 1
            # compare characters
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True