class Solution(object):
    def findMinArrowShots(self, points):
        """:type points: List[List[int]]
        :rtype: int"""
        if not points:
            return 0
        
        # Sort balloons by their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            # If the current balloon starts after the last arrow position, we need a new arrow
            if points[i][0] > arrow_pos:
                arrows += 1
                arrow_pos = points[i][1]
                
        return arrows