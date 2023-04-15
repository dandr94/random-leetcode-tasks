from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        _len = len(cost)

        if _len < 3:
            return sum(cost)

        cost.sort(reverse=True)
        res, i = 0, 0,
        while i < _len:
            res += sum(cost[i: i + 2])
            i += 3
        return res


sol = Solution()
print(sol.minimumCost(cost=[1, 2, 3]))
print(sol.minimumCost(cost=[6, 5, 7, 9, 2, 2]))
print(sol.minimumCost(cost=[5, 5]))

# Problem - https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/
