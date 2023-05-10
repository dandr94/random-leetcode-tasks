from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
        return profit


sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))

# Problem - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
