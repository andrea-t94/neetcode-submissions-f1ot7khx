class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        # move backward
        for i in range(n-1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i+1][False] - prices[i]
                    keep = dp[i+1][True]
                    dp[i][1] = max(buy, keep)
                else:
                    sell = dp[i+2][True] + prices[i] if i+2<n else prices[i]
                    keep = dp[i+1][False]
                    dp[i][0] = max(sell, keep)
        return dp[0][1]
