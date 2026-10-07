import heapq
class MedianFinder(object):

    def __init__(self):
        # Max-heap for the lower half of numbers (inverted values)
        self.small = []
        # Min-heap for the upper half of numbers
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Step 1: Add to max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance the sizes of the heaps (small can have at most 1 extra element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        # If total number of elements is odd, max-heap has the extra element
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        # If even, median is the average of both heap roots
        return (-self.small[0] + self.large[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()