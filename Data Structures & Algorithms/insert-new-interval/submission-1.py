from _bisect import bisect_left
from _bisect import bisect_right
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = bisect_left(intervals, newInterval[0], key=lambda interval : interval[0])
        # merge left
        if start - 1 >= 0 and intervals[start - 1][-1] >= newInterval[0]:
            intervals[start - 1][1] = max(intervals[start - 1][1], newInterval[1])
            start = start - 1
        else:
            intervals.insert(start, newInterval)

        curr = start + 1
        end = bisect_right(intervals, newInterval[1], key=lambda interval : interval[0])

        #merge right
        while curr < end:
            intervals[start][1] = max(intervals[curr][1], intervals[start][1])
            curr += 1

        del intervals[start + 1 : end]
        return intervals
