from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 設定 buy_price 為第一天的價格
        buy_price = prices[0]
        profit = 0

        # 使用迴圈遍歷每一天的價格
        # 如果當天的價格小於 buy_price，則更新 buy_price
        # 如果當天的價格減去 buy_price 大於 profit，則更新 profit
        
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)
        
        return profit