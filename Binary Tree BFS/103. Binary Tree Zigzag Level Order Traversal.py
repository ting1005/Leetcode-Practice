
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        queue = [root]
        left_to_right = True

        # 由 root 開始，每次取出 queue 的第一個節點，再將左子節點和右子節點加入 queue 中
        # 以 [3,9,20,null,null,15,7] 為例
        # 第一次child = 3，再將 9 和 20 加入 queue 中
          # result = [[3]]
        # 第二是child = 9，將 null 和 null 加入 queue 中，child = 20，將 15 和 7 加入 queue 中
          # result = [[3], [9, 20]]
        # 第三次 child = 15，將 null 和 null 加入 queue 中，child = 7，將 null 和 null 加入 queue 中
          # result = [[3], [9, 20], [15, 7]]

        mark = 0
        while queue:
            level_size = len(queue)
            children = []
            for _ in range(level_size):
                # 取出 queue 的第一個節點
                child = queue.pop(0)

                # 如果當前節點有左子節點或右子節點，則加入 children 中
                # 再將左子節點和右子節點加入 queue 中
                if child:
                    children.append(child.val)
                    queue.append(child.left)
                    queue.append(child.right)
            # 判斷children是否有值，有則加入判斷left_to_right是否為True，若是則reverse children
            if children:
                if not left_to_right:
                    children.reverse()
                result.append(children)
                
            left_to_right = not left_to_right

        return result            