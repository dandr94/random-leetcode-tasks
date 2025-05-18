from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a

        return b


sol = Solution()

print(sol.findCenter(edges=[[1, 2], [2, 3], [4, 2]]))

print(sol.findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))

# Easy
# https://leetcode.com/problems/find-center-of-star-graph/description/
