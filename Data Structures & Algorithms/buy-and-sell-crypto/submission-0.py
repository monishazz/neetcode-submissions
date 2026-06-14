class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]  # Best buy price so far
        max_profit = 0         # Best profit so far

        for price in prices:
            if price < min_price:
                min_price = price          # Found cheaper buy price!
            else:
                profit = price - min_price # What if we sell here?
                max_profit = max(max_profit, profit)  # Keep best profit

        return max_profit