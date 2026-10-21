class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def houserobber(houses):
            n = len(houses)
            dp = [0]*n
            if not houses:
                return 0
            if len(houses)==1:
                return houses[0]
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], houses[i]+dp[i-2])
            return dp[-1]
        return max(houserobber(nums[1:]), houserobber(nums[:-1]))

