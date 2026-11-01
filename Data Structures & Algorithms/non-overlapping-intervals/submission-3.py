class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals)
        prevEnd = sortedIntervals[0][1]
        removals = 0

        for interval in sortedIntervals[1:]:
            if prevEnd > interval[0]:
                removals += 1
                prevEnd = min(prevEnd, interval[1])
            else:
                prevEnd = interval[1]
        
        return removals
