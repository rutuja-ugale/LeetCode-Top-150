class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(list(cur))
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include the current candidate (can reuse it, so index stays `i`)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            # Skip the current candidate and move to the next index `i + 1`
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res