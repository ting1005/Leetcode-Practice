class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        """
        先將 nums 進行排序，並找出中位數的 index
        如果 nums 的長度是奇數，則直接返回中位數
        如果 nums 的長度是偶數，則返回中位數的平均值
        """
        self.nums.sort()
        idx = len(self.nums) // 2
        if len(self.nums) % 2 == 1:
            return self.nums[idx]
        else:
            return (self.nums[idx - 1] + self.nums[idx]) / 2
 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()