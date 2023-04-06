from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anc = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[anc], nums[i] = nums[i], nums[anc]
                anc += 1


sol = Solution()
print(sol.moveZeroes(nums=[0, 1, 0, 3, 12]))
print(sol.moveZeroes(nums=[0]))

# Problem - https://leetcode.com/problems/move-zeroes/description/
