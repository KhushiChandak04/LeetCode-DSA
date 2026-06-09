class MedianFinder(object):

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()