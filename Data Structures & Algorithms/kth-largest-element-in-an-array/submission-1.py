class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for number in nums:
            heapq.heappush(heap, number)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]