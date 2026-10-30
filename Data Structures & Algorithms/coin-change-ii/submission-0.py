class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i] = number of ways you achieve this amount using coins
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount]