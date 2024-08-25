class Solution:
    def climbStairs(self, n: int) -> int:
        # 建立一個長度為 n+1 的 list 來記錄每一階的走法
        dp = [0] * (n + 1)
        # 設定初始條件
        dp[0] = 1
        dp[1] = 1

        # 可以從 i - 1 爬一階或是從 i - 2 爬兩階
        # 因此 dp[i] = dp[i-1] + dp[i-2]
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]