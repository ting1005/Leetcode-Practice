from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 判斷 head 是否為空，如果是空，則回傳 head
        if not head: return head

        # 建立一個 list 來存放 head 的值，再使用將 head 的值存放到 head_list 中
        head_list = []
        current = head
        while current:
            head_list.append(current.val)
            current = current.next

        # 建立兩個 list 來存放小於 x 和大於 x 的值
        min_list = []
        max_list = []

        for num in head_list:
            if num < x:
                min_list.append(num)
            else:
                max_list.append(num)
        
        # 將 min_list 和 max_list 進行合併
        head_list = min_list + max_list

        # 建立一個新的 ListNode 來存放 head_list 的值
        result = ListNode(head_list[0])
        current = result

        for num in head_list[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return result
        
