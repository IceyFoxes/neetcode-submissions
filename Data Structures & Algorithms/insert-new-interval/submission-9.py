from _bisect import bisect_left
from _bisect import bisect_right
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = [interval[:] for interval in intervals]
        start = bisect_left(newIntervals, newInterval[0], key=lambda interval : interval[0])
        # merge left
        if start - 1 >= 0 and newIntervals[start - 1][-1] >= newInterval[0]:
            newIntervals[start - 1][1] = max(newIntervals[start - 1][1], newInterval[1])
            start = start - 1
        else:
            newIntervals.insert(start, newInterval)

        curr = start + 1
        end = bisect_right(newIntervals, newInterval[1], key=lambda interval : interval[0])

        #merge right
        while curr < end:
            newIntervals[start][1] = max(newIntervals[curr][1], newIntervals[start][1])
            curr += 1

        del newIntervals[start + 1 : end]
        return newIntervals
