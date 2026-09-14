class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path):
            # If the combination is done, add a copy of it to results
            if len(path) == k:
                res.append(path[:])
                return
            
            # Iterate through valid numbers from 'start' to 'n'
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop() # Backtrack

        backtrack(1, [])
        return res