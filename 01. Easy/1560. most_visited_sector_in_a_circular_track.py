from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first_round = rounds[0]
        last_round = rounds[-1]

        if first_round > last_round:
            return list(range(1, last_round + 1)) + list(range(first_round, n + 1))
        else:
            return list(range(first_round, last_round + 1))


sol = Solution()
print(sol.mostVisited(n=4, rounds=[1, 3, 1, 2]))
print(sol.mostVisited(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2]))
print(sol.mostVisited(n=7, rounds=[1, 3, 5, 7]))

# Problem - https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
