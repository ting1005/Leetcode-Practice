from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return nums[0]

        # 建立一個長度為 n 的 list 來記錄每一階的最大值
        dp = [0] * n
        # 設定初始條件
        # 第一階的最大值為 nums[0]
        # 第二階的最大值為 max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 透過迴圈計算每一階的最大值
        # 每一階的最大值為 max(前一階的最大值, 前兩階的最大值加上當前階的值)
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]