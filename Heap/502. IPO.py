import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 將 porfits 和 capital 進行排序，並將 profits 和 capital 進行配對
        projects = sorted(zip(capital, profits), key=lambda x:x[0])
        # max_capital 用來記錄當前的資本 W
        max_capital = w
        # heap 用來記錄當前所有資本小於等於 max_capital 的 profits
        heap = []

        # 每次遍歷選擇當前可以投資的 k 個 projects中 profits 最大的
        for _ in range(k):
            # 將符合條件的 profits 加入 heap，並將其從 projects 中移除
            while projects and projects[0][0] <= max_capital:
                heapq.heappush(heap, -projects.pop(0)[1])

            # 如果 heap 中沒有 projects，則返回 max_capital
            if not heap:
                return max_capital
            # 否則將 heap 中最大的 profits 加入 max_capital
            max_capital += -heapq.heappop(heap)

        return max_capital
