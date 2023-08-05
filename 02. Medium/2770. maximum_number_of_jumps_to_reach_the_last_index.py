from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if dp[j] >= 0 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]


sol = Solution()
print(sol.maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=2))
print(sol.maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=3))

# Problem - https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/
