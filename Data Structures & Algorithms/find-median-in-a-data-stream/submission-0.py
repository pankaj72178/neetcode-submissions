class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        if (len(self.arr) == 0):
            self.arr.append(num)
        
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] > num:
            self.arr[i+1] = self.arr[i]
            i -= 1
        self.arr[i+1] = num

    def findMedian(self) -> float:
        n = len(self.arr)
        if (n%2==0):
            t = n//2
            median = (self.arr[t]+self.arr[t-1])/2
        else:
            median = (self.arr[n//2])
        return median