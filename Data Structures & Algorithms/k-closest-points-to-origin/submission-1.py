class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for point in points:
            distance = pow(point[0], 2) + pow(point[1], 2)
            distances.append((distance, point))
        
        kSmallestDistance = heapq.nsmallest(k, distances)        
        kClosest = [point for _, point in kSmallestDistance]
        return kClosest