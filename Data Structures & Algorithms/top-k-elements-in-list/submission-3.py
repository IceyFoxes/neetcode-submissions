class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # convert to dict
        helper = defaultdict(int)
        for num in nums:
            helper[num] += 1
        
        heap = []
        for num, freq in helper.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for freq, num in heap:
            result.append(num)
        return result
