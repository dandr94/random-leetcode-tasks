class Solution:
    def divisorGame(self, n: int) -> bool:
        # return n % 2 == 0

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == 0:
                    dp[i] = 1
                    break

        return dp[n] == 1


sol = Solution()
print(sol.divisorGame(n=2))
print(sol.divisorGame(n=3))

# Problem - https://leetcode.com/problems/divisor-game/
