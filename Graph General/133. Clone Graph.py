from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        # 建立 Dictionary 來儲存已經複製過的節點
        old_to_new = {}

        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            """
              定義DFS函數進行深度優先搜尋

              args:
                node: Optional['Node'] : 當前節點

              returns:
                Optional['Node'] : 複製的節點
            """
            
            # 如果節點已經被複製過，則直接返回
            if node in old_to_new:
                return old_to_new[node]
            
            # 沒有被複製過的節點，則先建立此節點到 old_to_new
            copy = Node(node.val)
            old_to_new[node] = copy

            # 對當前節點的鄰居進行複製，並將複製的節點加入到 copy 的 neighbors 中
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
        