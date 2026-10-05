from typing import List
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = list(zip(capital, profits))
        heapq.heapify(projects)
        
        max_profit = []
        
        for _ in range(k):
            # Push all affordable projects into the max-heap (negating profits for max-heap behavior)
            while projects and projects[0][0] <= w:
                cap, prof = heapq.heappop(projects)
                heapq.heappush(max_profit, -prof)
            
            # If no projects can be afforded, break out
            if not max_profit:
                break
                
            # Pick the project with the maximum profit
            w += -heapq.heappop(max_profit)
            
        return w