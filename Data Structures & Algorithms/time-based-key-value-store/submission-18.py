from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.times = defaultdict(list)    # key -> [t1, t2, ...] sorted
        self.values = defaultdict(list)   # key -> [v1, v2, ...] same order

    def set(self, key, value, timestamp):
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        times = self.times.get(key, [])
        i = bisect_right(times, timestamp) - 1    # last index with time <= timestamp
        return self.values[key][i] if i >= 0 else ""





