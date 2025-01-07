class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        lowest = prices[0]

        for p in prices:
            lowest = min(lowest,p)
            max_prof = max(max_prof, p - lowest)

        return max_prof




    

















        
        # lowest = prices[0]
        # max_profit = 0

        # for price in prices:
        #     if price < lowest:
        #         lowest = price
        #     max_profit = max(max_profit, price - lowest)

        # return max_profit

        # # Time: O(n) Space: O(1)


