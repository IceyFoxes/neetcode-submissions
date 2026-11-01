"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        end = []
        meetingRooms = 0

        for interval in sorted(intervals, key=lambda interval : interval.start):
            # if meeting starts after the heap's first end
            while end and interval.start >= end[0]:
                heapq.heappop(end)
            # if overlap
            else:
                heapq.heappush(end, interval.end)
            meetingRooms = max(meetingRooms, len(end))
        
        return meetingRooms