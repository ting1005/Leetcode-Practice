from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 讓 result[0] 可以在 dfs 中被修改，所以用 list 包一層
        result = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            # 如果 root 是 None，回傳 0
            if root == None: return 0

            # 遞迴計算左右子樹的最大值，並確保最小值為 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            # 更新 result[0]，因為 result[0] 會被修改，所以用 max 來更新
            result[0] = max(result[0], root.val + left + right)
            
            # 回傳左右子樹的最大值
            return root.val + max(left, right)

        dfs(root)

        return result[0]