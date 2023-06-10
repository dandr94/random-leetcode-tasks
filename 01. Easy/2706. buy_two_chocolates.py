from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)

        lowest = money - prices[0] - prices[1]

        return lowest if lowest >= 0 else money


sol = Solution()
print(sol.buyChoco(prices=[1, 2, 2], money=3))
print(sol.buyChoco(prices=[3, 2, 3], money=3))

# Problem - https://leetcode.com/contest/biweekly-contest-105/problems/buy-two-chocolates/
