from collections import Counter


class Solution:
    def isFascinating(self, n: int) -> bool:
        conc = list(str(n) + str(n * 2) + str(n * 3))

        return '0' not in conc and len(conc) == len(set(conc))


sol = Solution()
print(sol.isFascinating(n=192))
print(sol.isFascinating(n=100))

# Problem - https://leetcode.com/problems/check-if-the-number-is-fascinating/description/
