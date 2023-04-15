from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums

        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2])[::-1]

        return nums


sol = Solution()
print(sol.sortEvenOdd(nums=[4, 1, 2, 3]))
print(sol.sortEvenOdd(nums=[2, 1]))

# Problem - https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
