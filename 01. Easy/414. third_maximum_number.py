from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        _set = set(nums)
        _sorted = sorted(_set)[::-1]
        return _sorted[2] if len(_sorted) > 2 else _sorted[0]


sol = Solution()
print(sol.thirdMax(nums=[3, 2, 1]))
print(sol.thirdMax(nums=[1, 2]))

# Problem - https://leetcode.com/problems/third-maximum-number/
