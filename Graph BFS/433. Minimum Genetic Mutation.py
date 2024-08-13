from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        options = ["A", "C", "G", "T"]
        
        queue = deque()
        queue.append(startGene)

        visited = set()
        visited.add(startGene)

        count = 0

        while queue:
            size = len(queue)
            # 使用迴圈遍歷此層的節點數量
            # 每次迭代處理此層的所有 gene，並嘗試對每個 gene進行變異
            # 如果變異後 gene 在 bank_set 中且未被訪問過，則將其加入 queue 並將其加入 visited
        
            for _ in range(size):
                # 取出 queue 中的第一個元素
                gene = queue.popleft()
                # 如果 gene 等於 endGene，則回傳 count
                if gene == endGene:
                    return count
                # 使用迴圈遍歷 gene 的每一個字母
                
                for j in range(8):
                    # 使用迴圈遍歷 options 中的每一個字母
                    for option in options:
                        # 將 gene 的第 j 個字母換成 option
                        new_gene = gene[:j] + option + gene[j+1:]
                        # 如果 new_gene 在 bank_set 中且 new_gene 不在 visited 中，則將 new_gene 加入 queue 並將 new_gene 加入 visited
                        if new_gene in bank_set and new_gene not in visited:
                            queue.append(new_gene)
                            visited.add(new_gene)

            count += 1

        return -1
