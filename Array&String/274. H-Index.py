from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # 將引用次數排序
        citations.sort()

        for idx, value in enumerate(citations):
            # 如果 n - idx 小於等於 (至少被 n - i 引用的文章數) value，則回傳 n - idx
            if n - idx <= value:
                return n - idx
        
        return 0