class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        # iterate through the list starting from the second day
        for i in range(1, len(prices)):
            # if today's price is higher than yesterday's, 
            # capture that profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit