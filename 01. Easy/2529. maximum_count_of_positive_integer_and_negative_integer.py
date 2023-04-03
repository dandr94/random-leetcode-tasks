from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)


sol = Solution()
print(sol.maximumCount(nums=[-2, -1, -1, 1, 2, 3]))
print(sol.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]))

# Problem - https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
