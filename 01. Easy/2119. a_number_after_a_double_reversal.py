class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not num or num % 10 != 0


sol = Solution()
print(sol.isSameAfterReversals(526))
print(sol.isSameAfterReversals(1800))
print(sol.isSameAfterReversals(0))

# Problem - https://leetcode.com/problems/a-number-after-a-double-reversal/description/
