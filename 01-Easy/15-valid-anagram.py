class Solution(object):
    def isAnagram(self, s, t):
        # Early Exit
        if len(s) != len(t):
            return False
        # Initialize Hash map
        count = {}
        # built character profile
        for char in s:
            count[char] = count.get[char, 0] + 1
            # validate character profile
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True