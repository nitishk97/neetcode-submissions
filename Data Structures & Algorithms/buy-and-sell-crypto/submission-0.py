class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            leastPrice = min(leastPrice, prices[i-1])
            profit = prices[i] - leastPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit
