from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        return sorted(set(nums))[1]


sol = Solution()
print(sol.findNonMinOrMax(nums=[3, 2, 1, 4]))
print(sol.findNonMinOrMax(nums=[1, 2]))
print(sol.findNonMinOrMax(nums=[2, 1, 3]))

# Problem - https://leetcode.com/problems/neither-minimum-nor-maximum/description/
