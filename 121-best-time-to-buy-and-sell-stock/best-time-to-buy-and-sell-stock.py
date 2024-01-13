class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            max_prof = max(max_prof, p - lowest)

        return max_prof





      