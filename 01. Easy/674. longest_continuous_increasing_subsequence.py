from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = c = 1
        for i in range(1, len(nums)):
            c = c + 1 if nums[i] > nums[i - 1] else 1

            res = max(res, c)

        return res


sol = Solution()
print(sol.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
print(sol.findLengthOfLCIS(nums=[2, 2, 2, 2, 2]))

# Problem - https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
