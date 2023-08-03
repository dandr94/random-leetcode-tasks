from typing import List
from math import sqrt


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for idx, num in enumerate(nums):
            if len(nums) % (idx + 1) == 0:
                res += num ** 2

        return res


sol = Solution()
print(sol.sumOfSquares(nums=[1, 2, 3, 4]))
print(sol.sumOfSquares(nums=[2, 7, 1, 19, 18, 3]))

# Problem - https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
