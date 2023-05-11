class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n
        #
        # dp = [0] * (n + 1)
        # dp[1], dp[2] = 1, 2
        #
        # i = 3
        #
        # while i < n + 1:
        #     dp[i] = dp[i - 1] + dp[i - 2]
        #     i += 1
        #
        # return dp[n]

        a, b = 1, 1

        for i in range(n - 1):
            x = a + b
            a, b = b, x

        return b


sol = Solution()
print(sol.climbStairs(n=2))
print(sol.climbStairs(n=3))

# Problem - https://leetcode.com/problems/climbing-stairs/description/
