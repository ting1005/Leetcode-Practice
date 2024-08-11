from typing import List, Set


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        # 將 equations 與 values 轉換成圖形
        # 例如 equations = [["a", "b"], ["b", "c"]], values = [2.0, 3.0]
        # 則 graph = {"a": {"b": 2.0}, "b": {"a": 0.5, "c": 3.0}, "c": {"b": 0.3333333333333333}}
        for idx, value in enumerate(equations):
            x, y = value
            if x not in graph: graph[x] = {}
            if y not in graph: graph[y] = {}

            graph[x][y] = values[idx]
            graph[y][x] = 1 / values[idx]

        def dfs(src: str, dst: str, visited: Set[str]) -> float:
            """
            透過深度優先搜尋，尋找 src 到 dst 的 value
            args:
                src: str, 起始點 (被除數)
                dst: str, 終點 (除數)
                visited: Set[str], 紀錄已經訪問過的點
            returns:
                float: src 到 dst 的 value
            """
            # 如果 src 或 dst 不在 graph 中，則回傳 -1.0
            # 如果 src 等於 dst，則回傳 1.0
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            #將 src 加入 visited 中，表示已經訪問過
            visited.add(src)

            # 透過深度優先搜尋，尋找 src 到 dst 的 value
            # 假設 src 為 a，dst 為 c，graph = {"a": {"b": 2.0}, "b": {"a": 0.5, "c": 3.0}, "c": {"b": 0.3333333333333333}}
            # 則先找出 a 到 b 的 value (2.0)，再找出 b 到 c 的 value (3.0)
            # 最後回傳 a 到 b 的 value 乘上 b 到 c 的 value
            for neighbor, value in graph[src].items():
                if neighbor in visited:
                    continue

                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return result * value
            # 如果找不到 src 到 dst 的 value，則回傳 -1.0
            return -1.0

        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))

        return results
