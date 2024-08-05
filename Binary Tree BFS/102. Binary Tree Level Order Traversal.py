from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        queue = [root]
        # 由 root 開始，每次取出 queue 的第一個節點，再將左子節點和右子節點加入 queue 中
        # 以 [3,9,20,null,null,15,7] 為例
        # 第一次child = 3，再將 9 和 20 加入 queue 中
          # result = [[3]]
        # 第二是child = 9，將 null 和 null 加入 queue 中，child = 20，將 15 和 7 加入 queue 中
          # result = [[3], [9, 20]]
        # 第三次 child = 15，將 null 和 null 加入 queue 中，child = 7，將 null 和 null 加入 queue 中
          # result = [[3], [9, 20], [15, 7]]

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

            # 如果 children 有值，則加入 result
            if children:
                result.append(children)

        return result            