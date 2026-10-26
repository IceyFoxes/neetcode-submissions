class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # max freq * interval length
        # consider how many distinct char can fit into 1 single interval
        # => else consider if total sum (excluding most freq) can fit into all intervals
        # => then lengthen each interval + 1 (modulus)

        frequency = Counter(tasks)
        heap = [(-count, character) for character, count in frequency.items()]
        heapq.heapify(heap)
        task_cooldown = []
        cycles = 0

        while heap or task_cooldown:
            while task_cooldown and cycles > n + task_cooldown[0][1]:
                finished_cooldown, _ = task_cooldown.pop()
                task = heapq.heappush(heap, finished_cooldown)
            
            if not heap:
                # Idle
                cycles += 1
                continue

            task = heapq.heappop(heap)    
            task_count = -task[0]
            task_char = task[1]

            task_count -= 1
            if task_count > 0:
                remaining_task = (-task_count, task_char)
                task_cooldown.append((remaining_task, cycles))
            
            cycles += 1
        return cycles

