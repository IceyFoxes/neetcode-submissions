class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequency = Counter(tasks)
        heap = [-count for _, count in frequency.items()]
        heapq.heapify(heap)
        task_cooldown = deque()
        cycles = 0

        while heap or task_cooldown:
            if task_cooldown and cycles > task_cooldown[0][1]:
                task_count, _ = task_cooldown.popleft()
                heapq.heappush(heap, task_count)
            
            if heap:
                task_count = heapq.heappop(heap) + 1
                if task_count < 0:
                    task_cooldown.append((task_count, cycles + n))
                cycles += 1

            # skip to next
            else:
                cycles = task_cooldown[0][1] + 1
        return cycles

