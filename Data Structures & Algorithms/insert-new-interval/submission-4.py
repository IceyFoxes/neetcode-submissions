class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        start, end = newInterval
        i = 0
        n = len(intervals)

        # Entirely before the new interval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Overlapping the new interval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        result.append([start, end])

        # Entirely after the merged interval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result