from typing import List
from collections import defaultdict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        _map = {}

        for i in range(n):
            for j in range(m):
                _map[mat[i][j]] = (i, j)

        row = [0] * n
        col = [0] * m

        for i in range(len(arr)):
            x = _map[arr[i]]
            row[x[0]] += 1
            col[x[1]] += 1
            if row[x[0]] == m or col[x[1]] == n:
                return i


sol = Solution()
print(sol.firstCompleteIndex(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]]))
print(sol.firstCompleteIndex(arr=[2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
print(sol.firstCompleteIndex(arr=[6, 2, 3, 1, 4, 5], mat=[[5, 1], [2, 4], [6, 3]]))

# Problem - https://leetcode.com/problems/first-completely-painted-row-or-column/description/
