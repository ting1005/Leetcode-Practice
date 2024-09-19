
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # 建立一個 st 來存放 inorder 的結果
        self.st = []
        self.inorder(root)

    def inorder(self, root):
        # 建立一個 inorder 的遞迴函數，用來將節點的值存放到 st 中
        if root is None: return
        self.inorder(root.left)
        self.st.append(root.val)
        self.inorder(root.right)

    
    def next(self) -> int:
        # 回傳 st 的第一個元素，並將其移除
        return self.st.pop(0)


    def hasNext(self) -> bool:
        # 如果 st 中有元素，回傳 True，否則回傳 False
        return len(self.st) > 0
