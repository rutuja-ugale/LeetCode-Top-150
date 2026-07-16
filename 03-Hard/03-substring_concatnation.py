class Solution(object):
    def findSubstring(self, s, words):
        # Return empty if input string or word list is empty
        if not s or not words:
            return []
        
        from collections import Counter
        
        # Calculate lengths and target frequency map
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result = []
        
        # If the string is shorter than the combined length of all words, return empty
        if len(s) < total_len:
            return []
        
        # Iterate through each possible offset to check all alignments
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            
            # Slide the window across the string
            while right + word_len <= len(s):
                # Extract the next word and increment its count
                word = s[right : right + word_len]
                right += word_len
                current_counts[word] += 1
                
                # If the word count exceeds the allowed limit, shrink from the left
                while current_counts[word] > word_counts[word]:
                    left_word = s[left : left + word_len]
                    current_counts[left_word] -= 1
                    left += word_len
                
                # If window size equals the total required length, store the start index
                if right - left == total_len:
                    result.append(left)
                    
        return result