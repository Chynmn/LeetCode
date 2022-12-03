class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0,1,2]
        if n <= 2: return n
        for i in range(3, n+2):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]