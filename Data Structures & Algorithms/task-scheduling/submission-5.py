class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxf = max(count.values())
        num_max = sum(1 for c in count.values() if c == maxf)   # tasks tied for most frequent

        frame = (maxf - 1) * (n + 1) + num_max
        return max(len(tasks), frame)