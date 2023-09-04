class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            one = dp[i - 1] + cost[i - 1]
            print(one)
            two = dp[i - 2] + cost[i - 2]
            print(two)
            dp[i] = min(one, two)

        return dp[len(cost)]