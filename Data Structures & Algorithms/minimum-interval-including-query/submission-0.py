import heapq

class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        sortedIntervals = sorted(intervals)
        sortedQueries = sorted(
            (query, idx) for idx, query in enumerate(queries)
        )

        i = 0
        heap = []
        answers = [-1] * len(queries)

        for query, idx in sortedQueries:
            # Add all intervals that have started
            while i < len(sortedIntervals) and sortedIntervals[i][0] <= query:
                start, end = sortedIntervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            # Discard expired intervals when they reach the top
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                answers[idx] = heap[0][0]

        return answers