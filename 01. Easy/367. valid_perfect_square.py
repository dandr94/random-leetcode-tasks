import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num).is_integer()


sol = Solution()
print(sol.isPerfectSquare(num=16))
print(sol.isPerfectSquare(num=14))

# Problem - https://leetcode.com/problems/valid-perfect-square/