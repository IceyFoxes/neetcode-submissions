class Solution:
    def climbStairs(self, n: int) -> int:
        even = 1
        odd = 1

        if n <= 1:
            return even
        
        for _ in range(n - 1):
            curr = even + odd
            even = odd
            odd = curr
        return curr