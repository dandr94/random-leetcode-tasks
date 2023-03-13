from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if len(arr) == 1:
            return arr[0]

        dp = [0] * (k + 1)

        for i in range(len(arr)):
            m = d = -float('inf')
            for j in range(0, min(k, i + 1)):
                m = max(arr[i - j], m)
                d = max(d, m * (j + 1) + dp[-j - 1])

            dp = dp[1:] + [d]

        return dp[-1]


sol = Solution()
print(sol.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
print(sol.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
print(sol.maxSumAfterPartitioning(arr=[1], k=1))

# Problem - https://leetcode.com/problems/partition-array-for-maximum-sum/description/
