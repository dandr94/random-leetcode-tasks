from itertools import combinations
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0

        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                res += 1

        return res


sol = Solution()
print(sol.countQuadruplets(nums=[1, 2, 3, 6]))
print(sol.countQuadruplets(nums=[3, 3, 6, 4, 5]))
print(sol.countQuadruplets(nums=[1, 1, 1, 3, 5]))

# Problem - https://leetcode.com/problems/count-special-quadruplets/
