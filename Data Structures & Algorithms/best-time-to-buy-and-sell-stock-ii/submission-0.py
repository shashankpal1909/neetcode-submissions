class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        profit = 0

        for price in prices:
            if price < sell:
                profit += sell - buy
                buy = price

            sell = price
        
        profit += sell - buy
        return profit
