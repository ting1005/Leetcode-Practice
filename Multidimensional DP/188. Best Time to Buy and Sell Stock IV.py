class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        
        length = len(prices)

        # 檢查 k 是否大於等於 n // 2，如果k非常大，則可以進行多次交易，可以使用貪心法
        if k >= length // 2:
            result = 0
            for i in range(1, length):
                if prices[i] > prices[i - 1]:
                    result += prices[i] - prices[i - 1]
            return result
        
        # 初始化 buy 和 sell
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            # 對每個價格更新每次交易的買入和賣出的最大收益
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        
        return sell[k]