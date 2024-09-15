
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # 如果 root 是 None，直接回傳
        if root is None: return 

        current = root
        while current is not None:
            # 如果當前節點有左子節點
            if current.left is not None:
                # 找到左子節點的最右節點
                last = current.left
                while last.right is not None:
                    last = last.right
                
                # 將當前節點的右子節點接到左子節點的最右節點
                last.right = current.right

                # 將當前節點的左子節點接到右子節點
                current.right = current.left
                current.left = None

            current = current.right