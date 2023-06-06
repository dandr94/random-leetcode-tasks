class Solution:
    memo = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.memo[n]


sol = Solution()
print(sol.fib(n=2))
print(sol.fib(n=3))
print(sol.fib(n=4))

# Problem - https://leetcode.com/problems/fibonacci-number/
