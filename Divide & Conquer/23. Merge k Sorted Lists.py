
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 先判斷 lists 是否為空，如果是則返回 None
        if not lists: return None

        # 建立一個空的 list 來存放所有的數字
        nums = []

        # 將所有 lists 中的數字取出來存放到 nums 中
        for linked_list in lists:
            while linked_list:
                nums.append(linked_list.val)
                linked_list = linked_list.next

        # 如果 nums 為空，則返回 None
        if not nums: return None
        
        # 將 nums 進行排序後，建立一個新的 ListNode 來存放排序後的數字
        nums.sort()
        result = ListNode(nums[0])
        current = result
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return result