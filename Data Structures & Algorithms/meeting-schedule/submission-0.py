"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = -1

        for interval in sorted(intervals, key=lambda interval : interval.start):
            if prevEnd > interval.start:
                return False
            prevEnd = interval.end
        
        return True
