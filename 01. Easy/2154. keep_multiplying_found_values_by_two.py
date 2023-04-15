from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)

        while original in nums:
            original *= 2

        return original


sol = Solution()
print(sol.findFinalValue(nums=[5, 3, 6, 1, 12], original=3))
print(sol.findFinalValue(nums=[2, 7, 9], original=4))

# Problem - https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
