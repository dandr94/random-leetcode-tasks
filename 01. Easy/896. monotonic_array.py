from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_asc = sorted(nums)
        sorted_desc = sorted(nums, reverse=True)

        return sorted_asc == nums or sorted_desc == nums


sol = Solution()
print(sol.isMonotonic(nums = [1,2,2,3]))
print(sol.isMonotonic(nums = [6,5,4,4]))
print(sol.isMonotonic(nums = [1,3,2]))

# Problem - https://leetcode.com/problems/monotonic-array/