from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化 dp list
        # dp[i] 代表組成金額 i 所需的最少硬幣數
        # dp[0] = 0 代表組成金額 0 不需要任何硬幣
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # 透過迴圈計算每一個金額所需的最少硬幣數
        for i in range(1, amount + 1):
            for c in coins:
                # 如果 i - c >= 0，代表可以用 c 這個硬幣湊出金額 i
                # 更新 dp[i] 為 min(dp[i], 1 + dp[i-c])，表示用 c 這個硬幣湊出金額 i 所需最少的數量
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        # 如果 dp[-1] 仍然是 amount + 1，代表無法湊出金額 amount，回傳 -1
        # 否則回傳 dp[-1]
        return dp[-1] if dp[-1] != amount + 1 else -1