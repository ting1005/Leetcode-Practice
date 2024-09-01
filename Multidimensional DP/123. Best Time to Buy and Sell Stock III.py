from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        # 初始化，設定第一次和第二次的買入價格和賣出價格
        first_buy = float('-inf')
        first_sell = 0

        second_buy = float('-inf')
        second_sell = 0


        for price in prices:
            # 分別跟新第一次和第二次的買入價格和賣出價格
            # 第一次的買入價格為最大化買入的收益 (負收益)
            # 第一次的賣出價格為第一次交易中賣出股票後的最大收益
            # 第二次的買入價格為基於第一次的交易後的收益再次買入股票的成本
            # 第二次的賣出價格為第二次交易中賣出股票後的最大收益
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)

            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell