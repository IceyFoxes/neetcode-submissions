class MedianFinder:

    def __init__(self):
        # by enforcing the invariant that the max from the left side < min from the right side 
        # AND that |len(left side) - len(right side)| <= 1
        # we know the middle is always the median (either the mean of the 2 numbers), 
        # or the max/min from the side with 1 more number

        # maxHeap
        self.left = []
        # minHeap
        self.right = []
        self.lenLeft = 0
        self.lenRight = 0


    def addNum(self, num: int) -> None:
        # Figure out which heap num gets added to
        if not self.left or num <= -self.left[0]:
            # add to left if empty or smaller
            heapq.heappush(self.left, -num) 
        else:
            # add to right
            heapq.heappush(self.right, num)
        
        # balance the lengths of the 2 heaps
        leftLen = len(self.left)
        rightLen = len(self.right)

        if leftLen - rightLen > 1:
            leftMax = -heapq.heappop(self.left)
            heapq.heappush(self.right, leftMax)
        if rightLen - leftLen > 1:
            rightMin = heapq.heappop(self.right)
            heapq.heappush(self.left, -rightMin)

    def findMedian(self) -> float:
        leftLen = len(self.left)
        rightLen = len(self.right)

        if leftLen < rightLen:
            return self.right[0]
        elif leftLen > rightLen:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2