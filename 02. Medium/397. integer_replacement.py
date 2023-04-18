class Solution:
    memo = {1: 0}

    def integerReplacement(self, n: int) -> int:

        if n in self.memo:
            return self.memo[n]
        if n % 2 == 0:
            self.memo[n] = 1 + self.integerReplacement(n // 2)
            return self.memo[n]
        else:
            self.memo[n] = min(1 + self.integerReplacement(n + 1), 1 + self.integerReplacement(n - 1))
            return self.memo[n]


sol = Solution()
print(sol.integerReplacement(n=8))
print(sol.integerReplacement(n=7))
print(sol.integerReplacement(n=4))

# Problem - https://leetcode.com/problems/integer-replacement/description/
