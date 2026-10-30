class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 options we can choose
        # at each index, 
        # 1. we are allowed to buy or sell 
        # or
        # 2. we can skip/cooldown period
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):

            buy_option = dp[i+1][0]-prices[i]
            cooldown = dp[i+1][1]
            dp[i][1] = max(buy_option, cooldown)

            sell_option = dp[i+2][1]+prices[i]
            cooldown = dp[i+1][0]
            dp[i][0] = max(sell_option, cooldown)
        return dp[0][1]
