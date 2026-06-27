class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # create a dictionary to store frequencies of characters in magazine
        char_counts = {}
        # populate the inventory(the magazine)
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
        # check if the note can be constructed
        for char in ransomNote:
            # if the char is not in magazine or we ran out of that char
            if char_counts.get(char, 0) == 0:
                return False
            # use the character
            char_counts[char] -= 1
        return True