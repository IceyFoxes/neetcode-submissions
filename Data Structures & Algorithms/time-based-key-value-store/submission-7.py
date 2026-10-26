class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        ls = self.data[key]
        
        low = 0
        high = len(ls) - 1
        res = ""

        while low <= high:
            mid = low + (high - low) // 2
            timestamp_prev = ls[mid][1]

            if timestamp_prev <= timestamp:
                res = ls[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        
        return res
