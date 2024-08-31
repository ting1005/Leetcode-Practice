from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 判斷 head 是否為空，或是 head.next 是否為空，或是 k 是否為 0
        if not head or not head.next or k == 0: return head

        # 建立一個 list 來存放 head 的值，再使用將 head 的值存放到 head_list 中
        head_list = []
        current = head

        while current:
            head_list.append(current.val)
            current = current.next

        # 先將 k 取餘數，再判斷是否為 0，如果是 0，則回傳 head
        tail = k % len(head_list)
        if tail == 0: return head
        
        # 將 head_list 進行旋轉
        head_list = head_list[-tail:] + head_list[:(len(head_list) - tail)]

        # 建立一個新的 ListNode 來存放 head_list 的值
        result = ListNode(head_list[0])
        current = result

        for num in head_list[1:]:
            current.next = ListNode(num)
            current = current.next

        return result