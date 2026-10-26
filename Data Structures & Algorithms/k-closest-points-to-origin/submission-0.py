class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for idx in range(len(points)):
            point = points[idx]
            distance = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
            distances.append((distance, idx, point))
        
        kSmallestDistance = heapq.nsmallest(k, distances)        
        kClosest = [point for _, _, point in kSmallestDistance]
        return kClosest