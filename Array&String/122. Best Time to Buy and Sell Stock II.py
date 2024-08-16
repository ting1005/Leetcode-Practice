from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # 如果當天的價格比前一天的價格高，則賺取差價
        # 例如 prices = [7, 1, 5, 3, 6, 4]
        # 則 profit = (5 - 1) + (6 - 3) = 7
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit