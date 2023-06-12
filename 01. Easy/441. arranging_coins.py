class Solution:
    def arrangeCoins(self, n: int) -> int:
        j = 0

        while n >= 0:
            j += 1
            n -= j

        return j - 1


sol = Solution()
print(sol.arrangeCoins(n=5))
print(sol.arrangeCoins(n=8))

# Problem - https://leetcode.com/problems/arranging-coins/
