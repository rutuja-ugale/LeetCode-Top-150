class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(s, open_count, close_count):
            # If the current string has reached the maximum length
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # We can add an opening parenthesis if we haven't used all n of them
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # We can add a closing parenthesis if it won't exceed the opening count
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res