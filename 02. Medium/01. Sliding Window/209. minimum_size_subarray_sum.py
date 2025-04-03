from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


sol = Solution()
print(sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))

# Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
