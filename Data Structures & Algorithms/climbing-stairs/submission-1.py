class Solution:
    def climbStairs(self, n: int) -> int:
        # n = n - 1 + n - 2
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]