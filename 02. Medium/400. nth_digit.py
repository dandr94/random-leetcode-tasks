class Solution:
    def findNthDigit(self, n: int) -> int:
        start, digits = 1, 1
        while n > 9 * start * digits:
            n -= 9 * start * digits
            start = 10 ** digits
            digits += 1
        q, r = divmod(n - 1, digits)
        return int(str(start + q)[r])


sol = Solution()
print(sol.findNthDigit(n=3))
print(sol.findNthDigit(n=11))

# Problem - https://leetcode.com/problems/nth-digit/description/
