from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        if nums[0] == 1 and nums[-1] == len(nums):
            return 0

        res = 0

        one_idx = nums.index(1)
        max_idx = nums.index(len(nums))
        if one_idx < max_idx:
            res = one_idx + len(nums) - 1 - max_idx

        if one_idx > max_idx:
            res = one_idx + len(nums) - 1 - max_idx - 1

        return res


sol = Solution()
print(sol.semiOrderedPermutation(nums=[2, 1, 4, 3]))
print(sol.semiOrderedPermutation(nums=[2, 4, 1, 3]))
print(sol.semiOrderedPermutation(nums=[1, 3, 4, 2, 5]))

# Problem - https://leetcode.com/problems/semi-ordered-permutation/description/
