class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        # 初始化一個 Queue，用來保存每一層的節點。首先將根節點放入 Queue 中
        queue = [root]

        while queue:
            next_level = []
            for i in range(len(queue)):
                node = queue[i]

                # 將當前節點的 next 指針指向這一層的下一個節點
                if i < len(queue) - 1:
                    node.next = queue[i + 1]

                # 如果當前節點有左子節或右子節，則加入 next_level 列表中
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # 更新 queue，進入下一層
            queue = next_level
        return root