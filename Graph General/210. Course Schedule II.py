from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        result = []

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            

            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visited[course] = 2
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result[::-1]