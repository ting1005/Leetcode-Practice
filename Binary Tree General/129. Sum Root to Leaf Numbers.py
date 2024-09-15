from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 建立一個 DFS Function，並且帶入當前節點和數字
        # 利用 DFS 的方式，將數字乘以 10 加上當前節點的值
        # 如果當前節點是葉節點，回傳數字
        # 如果當前節點不是葉節點，繼續遞迴左右子節點
        def dfs(node: Optional[TreeNode], num: int) -> int:
            if not node: return 0

            num = num * 10 + node.val

            if not node.left and not node.right: return num
            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)