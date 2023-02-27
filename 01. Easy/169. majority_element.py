from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()

        return nums[len(nums) // 2]


sol = Solution()
print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))

# Problem - https://leetcode.com/problems/majority-element/description/
