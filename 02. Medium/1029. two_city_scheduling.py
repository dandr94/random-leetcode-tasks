from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        :return: an integer representing the minimum cost to fly all people to two cities such that exactly
                    `len(costs)//2` people fly to each city.
        """

        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        n = len(costs) // 2

        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total


sol = Solution()
print(sol.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))
print(sol.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))

# Problem - https://leetcode.com/problems/two-city-scheduling/
