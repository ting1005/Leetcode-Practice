from collections import Counter
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 建立一個 list 來存放 head 的值
        head_list = []

        # 將 head 的值存放到 list 中
        current = head
        while current:
            head_list.append(current.val)
            current = current.next
        
        # 使用 Counter 來計算 list 中每個值的數量
        # 如果值的數量為 1，則將其加入到 head_list 中
        head_list = Counter(head_list)
        head_list = [i for i in head_list if head_list[i] == 1]

        # 如果 head_list 為空，則回傳 None
        if not head_list: return None

        # 建立一個新的 ListNode 來存放 head_list 的值
        result = ListNode(head_list[0])
        current = result

        for num in head_list[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return result