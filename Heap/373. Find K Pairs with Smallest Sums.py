import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []

        heap = []
        result = []

        # 將初始化的 k 個 pairs 加入 heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i,0))

        # 從 heap 中取出最小的 pair，並將其加入 result 中，確保 result 保持最小的 pair
        while k > 0 and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result