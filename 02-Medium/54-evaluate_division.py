from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        # Step 2: Define DFS function to find path product from source to target
        def dfs(curr, target, visited, current_product):
            if curr == target:
                return current_product
            
            visited.add(curr)
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited, current_product * weight)
                    if result != -1.0:
                        return result
                        
            return -1.0

        # Step 3: Evaluate each query
        answers = []
        for c, d in queries:
            if c not in graph or d not in graph:
                answers.append(-1.0)
            elif c == d:
                answers.append(1.0)
            else:
                answers.append(dfs(c, d, set(), 1.0))
                
        return answers