from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # prefix 用於記錄每個索引左邊的乘積
        # suffix 用於記錄每個索引右邊的乘積
        # answer 用於記錄每個索引左右乘積的結果
        prefix = [1] * n
        suffix = [1] * n
        answer = []

        
        for i in range(1, n):
            # 利用 prefix[i] = prefix[i - 1] * nums[i - 1] 計算每個索引左邊的乘積
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            # 利用 suffix[i] = suffix[i + 1] * nums[i + 1] 計算每個索引右邊的乘積
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            # 將左右乘積相乘，得到每個索引左右乘積的結果
            answer.append(prefix[i] * suffix[i])

        return answer