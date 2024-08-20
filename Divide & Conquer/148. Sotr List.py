from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果 head 為空，則返回 None
        if not head: return head

        # 建立一個 node 來遍歷所有的節點，並將所有的值存放到 res_list 中
        node = head
        res_list = []
        while node:
            res_list.append(node.val)
            node = node.next
        
        # 將 res_list 進行排序
        res_list.sort()

        # 將排序後的值存放到原本的 ListNode 中
        node = head
        for val in res_list:
            node.val = val
            node = node.next
        
        return head