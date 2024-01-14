class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = 0

        for idx,curr in enumerate(prices):
            if curr < prices[lowest]:
                lowest = idx
            max_profit = max(max_profit, curr - prices[lowest])

        return max_profit