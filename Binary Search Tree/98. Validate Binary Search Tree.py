from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node: return True

            # 如果 node.val 小於等於 min_val 或 node.val 大於等於 max_val 則返回 False
            if (min_val is not  None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False
            
            # 檢查左子樹和右子樹
            # 左子樹的最大值為當前節點的值，右子樹的最小值為當前節點的值
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)
            
        return is_valid(root, float('-inf'), float('inf'))