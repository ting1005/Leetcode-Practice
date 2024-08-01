from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 = nums1[:m] + nums2
        nums1[m:] = nums2
        # .sort() is in-place sorting -> return None
        # sorted() is not in-place sorting -> return a new list
        nums1.sort()
        