from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_cost = sum(cost)
        sum_gas = sum(gas)

        # 如果成本大於瓦斯用量，則無法環繞一圈，返回 -1
        if sum_cost > sum_gas: return -1

        current_gas = 0
        start_index = 0

        for i in range(len(gas)):
            # 更新當前瓦斯量
            # 如果當前瓦斯不足以到達下一個加油站，則更新起始索引為下一個加油站
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1
        
        return start_index