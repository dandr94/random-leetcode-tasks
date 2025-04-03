from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        max_length = 1

        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                max_length = max(max_length, right - left)
                left = right

        return max(max_length, len(nums) - left)


sol = Solution()
print(sol.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
print(sol.findLengthOfLCIS(nums=[2, 2, 2, 2, 2]))
print(sol.findLengthOfLCIS(nums=[1, 3, 5, 7]))

# Easy
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
