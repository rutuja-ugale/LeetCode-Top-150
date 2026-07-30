class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1] keeps track of the current sign context
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0
                
        return ans + sign * num