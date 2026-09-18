class Solution:
    def maxProfit(self, prices):
        mn = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            else:
                profit = max(profit, prices[i] - mn)

        return profit