
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x: int, y: int, length: int) -> Node:
            """
            建立一個用來遞迴建立四叉樹的函數
            處理當前正方形區域是單個元素的情況，直接返回一個葉子節點
            如果當前區域不是單個元素，則遞迴建立四個子區域
            如果四個子區域都是葉子節點，且四個子區域的值相同，則合併為一個葉子節點，否則返回一個非葉子節點
            args:
                x: int, 當前區域的左上角 x 座標
                y: int, 當前區域的左上角 y 座標
                length: int, 當前區域的邊長
            return: 
                Node: 四叉樹的根節點
            """
            if length == 1:
                return Node(grid[x][y] == 1, True)
            
            half = length // 2
            top_left = build(x, y, half)
            top_right = build(x, y + half, half)
            bottom_left = build(x + half, y, half)
            bottom_right = build(x + half, y + half, half)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True)
            else:
                return Node(True, False, top_left, top_right, bottom_left, bottom_right)
            
        return build(0, 0, len(grid))