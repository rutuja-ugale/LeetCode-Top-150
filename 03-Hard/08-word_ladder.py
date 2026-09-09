from collections import deque
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        
        # If the end word is not in the dictionary, no transformation sequence is possible
        if endWord not in wordSet:
            return 0
            
        # Queue stores tuples of (current_word, current_level)
        queue = deque([(beginWord, 1)])
        
        while queue:
            curr_word, level = queue.popleft()
            
            # If we reach the target word, return the total length of the sequence
            if curr_word == endWord:
                return level
                
            # Try changing each character position from 'a' through 'z'
            for i in range(len(curr_word)):
                for ch in string.ascii_lowercase:
                    # Skip if it's the same character
                    if ch == curr_word[i]:
                        continue
                        
                    next_word = curr_word[:i] + ch + curr_word[i+1:]
                    
                    # If the new word is a valid transformation, push to queue and remove from set
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, level + 1))
                        
        return 0