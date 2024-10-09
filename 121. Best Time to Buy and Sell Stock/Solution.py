class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_n = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < min_n:
                min_n = prices[i]
            else:
                if prices[i] - min_n > profit:
                    profit = prices[i] - min_n
        return profit
        