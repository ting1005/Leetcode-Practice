from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # 每個小孩都先個別給一顆糖果
        candies = [1] * n

        # 從左到右，如果右邊的小孩比左邊的小孩分數高，則右邊的小孩糖果數比左邊的小孩多一顆
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # 從右到左，如果左邊的小孩比右邊的小孩分數高，則比較左右兩邊的糖果數，取較大的糖果數
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)