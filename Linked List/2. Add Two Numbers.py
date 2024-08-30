from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化 temp 來存放進位的值
        temp = 0
        result = ListNode(0)
        current = result

        # 當 l1 和 l2 都不為 None 或 temp 不為 0 時，進行以下操作
        while l1 is not None or l2 is not None or temp != 0:
            # 如果 l1 和 l2 都不為 None，則取出其值
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # 計算 l1_val + l2_val + temp 的值
            value = l1_val + l2_val + temp
            
            # 將 value % 10 加入到 current.next 中
            current.next = ListNode(value % 10)
            # 將 current 指向 current.next
            current = current.next
            # 將 temp 設為 value // 10
            temp = value // 10

            # 如果 l1 不為 None，則將 l1 指向 l1.next
            # 如果 l2 不為 None，則將 l2 指向 l2.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        # 回傳 result.next，因為 result 的第一個值為 0
        return result.next            