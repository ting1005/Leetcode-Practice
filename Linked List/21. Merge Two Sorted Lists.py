from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 建立一個 list 來存放 list1 和 list2 的值
        sorted_list = []

        # 將 list1 和 list2 的值存放到 sorted_list 中
        while list1 or list2:
            if list1: 
                sorted_list.append(list1.val)
                list1 = list1.next
            if list2:
                sorted_list.append(list2.val)
                list2 = list2.next
        # 將 sorted_list 進行排序
        sorted_list.sort()
        # 如果 sorted_list 為空，則回傳 None
        if not sorted_list: return None

        # 建立一個新的 ListNode 來存放 sorted_list 的值
        result = ListNode(sorted_list[0])
        current = result
        # 將 sorted_list 的值存放到 result 中
        for num in sorted_list[1:]:
            current.next = ListNode(num)
            current = current.next

        return result