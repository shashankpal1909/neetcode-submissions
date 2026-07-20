class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -1
        profit = 0

        for price in prices:
            if buy == -1:
                buy = price
                continue

            if price < buy:
                buy = price
            else:
                profit = max(0, profit, price - buy)

        return profit
