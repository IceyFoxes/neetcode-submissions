class TimeMap:

    def __init__(self):
        # stores key (name) : list of (timestamp, value)
        self.storage = defaultdict(list)
        
    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # insert O(1)
        self.storage[key].append((timestamp, value))
        return


    # O(log N)
    def get(self, key: str, timestamp: int) -> str:
        array = self.storage[key]
        # binary search
        low = 0
        high = len(array) - 1

        if not array or timestamp < array[low][0]:
            return ""

        while low < high:
            mid = low + (high - low + 1) // 2
            curr = array[mid][0]

            if timestamp < curr:
                high = mid - 1
            else:
                low = mid
        
        return self.storage[key][low][1]






