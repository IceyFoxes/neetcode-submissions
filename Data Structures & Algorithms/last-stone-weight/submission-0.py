class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            result = first - second

            if result:
                heapq.heappush(stones, -result)
        
        if stones:
            return -stones[0]
        else:
            return 0
        
        