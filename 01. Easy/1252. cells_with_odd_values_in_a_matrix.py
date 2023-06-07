from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for row, col in indices:
            rows[row] += 1
            cols[col] += 1

        return sum([(r + c) % 2 for c in cols for r in rows])


sol = Solution()
print(sol.oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(sol.oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))

# Problem - https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/
