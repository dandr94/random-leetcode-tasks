from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_average_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_average_sum = max(max_average_sum, current_sum)

        return max_average_sum / k


sol = Solution()
print(sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(sol.findMaxAverage(nums=[5], k=1))

# Easy
# https://leetcode.com/problems/maximum-average-subarray-i/
