class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in dp:
                return dp[(i, holding)]
            
            keep = dfs(i+1, holding)
            if holding:
                # I can sell
                sell = prices[i] + dfs(i+2, not holding)
                dp[(i, holding)] = max(keep, sell)
            else:
                # I can buy
                buy = dfs(i+1, not holding) - prices[i]
                dp[(i, holding)] = max(keep, buy)
            
            return dp[(i, holding)]
        dp = {}
        return dfs(0, False)
