from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


sol = Solution()
print(sol.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(sol.pivotIndex(nums=[1, 2, 3]))
print(sol.pivotIndex(nums=[2, 1, -1]))

# Problem - https://leetcode.com/problems/find-pivot-index/
