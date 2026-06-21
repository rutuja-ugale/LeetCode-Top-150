class Solution(object):
    def maxProfit(self, prices):
        # initialize min_price to infinity and max_profit  to 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # update min_price if a lower price is found
            if price < min_price:
                min_price = price
                # Calculate profit and update max_profit if it's the highest seen
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit