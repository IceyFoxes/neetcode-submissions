class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        purchasePrice = prices[0]

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - purchasePrice)
            purchasePrice = min(purchasePrice, prices[i])
        
        return maxProfit