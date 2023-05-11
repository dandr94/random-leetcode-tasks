import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_el = nums[mid]

            if mid_el == target:
                return mid

            if mid_el > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


sol = Solution()
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=2))

# Problem - https://leetcode.com/problems/binary-search/
