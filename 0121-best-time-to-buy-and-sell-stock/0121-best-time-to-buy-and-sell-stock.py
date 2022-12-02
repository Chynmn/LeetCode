class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        
        for price in prices:
            if price < min:
                min = price
                
            if price - min > profit:
                profit = price - min

        return profit