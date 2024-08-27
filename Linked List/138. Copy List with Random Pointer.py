from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        old_to_new = {}

        # 建立一個 Hash map 來對應舊的 Node 和新的 Node
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        # 透過 Hash map 來對應舊的 Node 的 next 和 random 指向新的 Node
        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)

            current = current.next
        
        # 返回新的Linked List頭節點
        return old_to_new[head]