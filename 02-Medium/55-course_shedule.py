class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: Build the adjacency list
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            
        # Step 2: Track visit states
        # 0 = Unvisited
        # 1 = Visiting (currently in the current recursion stack / path)
        # 2 = Visited (fully processed, no cycles found)
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == 1:
                return False  # Cycle detected!
            if visited[node] == 2:
                return True   # Already checked and safe
                
            visited[node] = 1  # Mark as currently visiting
            
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
                    
            visited[node] = 2  # Mark as fully visited
            return True

        # Step 3: Check every course (handles disconnected graphs)
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True