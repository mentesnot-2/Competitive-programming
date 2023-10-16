class MedianFinder:

    def __init__(self):
        self.data = []
    def addNum(self, num: int) -> None:
        l,r = 0,len(self.data)
        while l < r:
            mid = l + (r - l) // 2
            if self.data[mid] < num:
                l = mid + 1
            else:
                r = mid
        self.data.insert(l,num)
        
    def findMedian(self) -> float:
        n = len(self.data)
        if len(self.data) % 2 != 0:
            return float(self.data[n // 2])
        else:
            middle_right = self.data[n // 2]
            middle_left = self.data[n // 2 - 1]
            return (middle_left + middle_right) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()