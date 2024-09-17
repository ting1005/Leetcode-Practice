from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        # 用來標記每個節點狀態
        # 0: 未訪問，1: 訪問中，2: 已訪問
        visited = [0] * numCourses

        # 統計每個節點的入度和出度
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(course):
            # 如果在訪問過程發現有環，則返回 False，表示無法完成所有課程
            if visited[course] == 1:
                return False
            # 如果節點已經訪問過，則直接返回 True
            if visited[course] == 2:
                return True
            
            # 標記節點為訪問中
            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                
            # 標記節點為已訪問
            visited[course] = 2
            return True
        # 對每個節點進行 DFS
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True