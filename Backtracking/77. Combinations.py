from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start: int) -> None:
            """
            建立一個遞迴函數來尋找所有可能的組合
            如果 combine 的長度等於 k，則將 combine 加入到 result 中並返回
            否則將 num 加入到 combine 中，並將num + 1後遞迴下去
            遞迴完成後再將 num 移除
            args:
                start: int, 目前的索引
            return:
                None
            """
            if len(combine) == k:
                result.append(combine[:])
                return
            
            for num in range(start, n + 1):
                combine.append(num)
                backtrack(num + 1)
                combine.pop()

        result = []
        combine = []
        backtrack(1)

        return result