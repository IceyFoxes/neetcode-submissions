class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # since h >= piles.length
        high = max(piles)
        # hypothetical minimum
        low = 1
        
        def check(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            return time <= h
        
        # binary search from low to high for smallest valid
        while low < high:
            mid = low + (high - low) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low