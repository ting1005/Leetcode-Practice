from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depth = 0
        
        def rightSide(root: Optional[TreeNode] , result: List[int] , depth: int) -> None:
            """
            A recursive function to get the right side view of the binary tree.
            Args:
                root (Optional[TreeNode]): The root of the binary tree
                result (List[int]): The result of the right side view of the binary tree
                depth (int): The depth of the binary tree
            """
            if root == None: return

            # 如果 result 的長度等於當前的深度，則將當前節點的值加入 result 中
            # 以 [1,2,3,null,5,null,4] 為例
            # 當深度為 0 時，root result = [1]
            # 當深度為 1 時，result = [1, 3]
            # 當深度為 2 時，result = [1, 3, 4]

            if len(result) == depth:
                result.append(root.val)

            
            depth += 1      
            # 因為需要從右邊開始看，所以先遞迴檢查右子樹，再遞迴檢查左子樹
            # 以例子來看，到了深度為 3 時，右子樹會因為為 None 而返回，再遞迴檢查左子樹
            rightSide(root.right , result , depth)
            rightSide(root.left , result , depth)

        # 初始遞迴，從根節點開始，深度為 0
        rightSide(root , result , depth)

        return result 
        