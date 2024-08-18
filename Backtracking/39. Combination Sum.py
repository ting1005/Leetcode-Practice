from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(idx: int, combin: List[int], total: int) -> List[List[int]]:
            """
            尋找所有總合為 target 的組合
            先判斷 total 是否等於 target，如果是則將 combin 加入到 result 中
            如果 total 大於 target 或者 idx 大於 candidates 的長度，則返回
            將 candidates[idx] 加入到 combin 中，並且遞迴下去
            之後將 candidates[idx] 移除，並且遞迴下去
            args:
                idx: 目前 candidates 的索引
                combin: 目前的組合
                total: 目前組合的總和
            return:
                result: 所有總和為 target 的組合
            """
            if total == target:
                result.append(combin[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            combin.append(candidates[idx])
            backtracking(idx, combin, total + candidates[idx])
            combin.pop()
            backtracking(idx + 1, combin, total)

            return result
        
        return backtracking(0, [], 0)