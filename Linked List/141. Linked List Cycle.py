from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 使用快慢指針，slow(head) 每次走一步，fast 每次走兩步
        fast = head

        # 如果 fast 或 fast.next 為 None，則表示沒有 cycle
        while fast and fast.next:
            
            head = head.next
            fast = fast.next.next
            # 如果 head 和 fast 相等，則表示有 cycle
            if head == fast:
                return True
            
        return False