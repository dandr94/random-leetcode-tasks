from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankings = {}

        for idx, num in enumerate(sorted(set(arr))):
            rankings[num] = idx + 1

        return list(map(rankings.get, arr))


sol = Solution()
print(sol.arrayRankTransform(arr=[40, 10, 20, 30]))
print(sol.arrayRankTransform(arr=[100, 100, 100]))
print(sol.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))

# Problem - https://leetcode.com/problems/rank-transform-of-an-array/description/
