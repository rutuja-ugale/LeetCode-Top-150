class Solution(object):
    def isValid(self, s):
        """:type s: str
        :rtype: bool"""
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top element from stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to the stack
                stack.append(char)
                
        # If the stack is empty, all brackets matched
        return not stack