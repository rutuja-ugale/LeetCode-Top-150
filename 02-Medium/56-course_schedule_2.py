class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque, defaultdict

        # Step 1: Build the adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Step 2: Initialize queue with courses having 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        # Step 3: Process the queue (BFS topological sort)
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses can be finished (no cycles)
        return result if len(result) == numCourses else []