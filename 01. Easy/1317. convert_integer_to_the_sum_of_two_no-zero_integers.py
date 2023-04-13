from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' not in f'{i}{n - i}':
                return [i, n - i]


sol = Solution()
print(sol.getNoZeroIntegers(n=2))
print(sol.getNoZeroIntegers(n=11))

# Problem - https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
