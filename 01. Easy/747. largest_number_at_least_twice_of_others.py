from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = nums.index(max(nums))
        max_num = nums.pop(max_idx)

        nums.sort()

        return max_idx if max_num >= nums[-1] * 2 else -1


sol = Solution()
print(sol.dominantIndex(nums=[3, 6, 1, 0]))
print(sol.dominantIndex(nums=[1, 2, 3, 4]))

# Problem - https://leetcode.com/problems/largest-number-at-least-twice-of-others/
