from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to hold lists of anagrams, where the key is the sorted string
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to create a canonical key
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped anagram lists
        return list(anagram_map.values())