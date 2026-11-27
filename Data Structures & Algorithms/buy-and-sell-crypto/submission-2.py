class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start at first day to buy
        # Iterate through rest of array, and if the
        # buy price is higher than the next day's price,
        # you automatically have a lower entry price
        buyPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if buyPrice > prices[i]:
                buyPrice = prices[i]
            maxProfit = max(maxProfit, prices[i] - buyPrice)
        return maxProfit