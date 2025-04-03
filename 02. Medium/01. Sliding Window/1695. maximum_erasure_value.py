from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        max_sum = 0
        curr_sum = 0
        unique_nums = set()

        for right in range(len(nums)):
            while nums[right] in unique_nums:
                unique_nums.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            unique_nums.add(nums[right])
            curr_sum += nums[right]

            max_sum = max(max_sum, curr_sum)

        return max_sum


sol = Solution()
print(sol.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(sol.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))

# Medium
# https://leetcode.com/problems/maximum-erasure-value/description/
