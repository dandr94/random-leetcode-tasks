from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, p = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        p += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        p += 1
                    if i == m - 1 or grid[i + 1][j] == 0:
                        p += 1
                    if j == n - 1 or grid[i][j + 1] == 0:
                        p += 1

        return p


sol = Solution()
print(sol.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(sol.islandPerimeter(grid=[[1]]))
print(sol.islandPerimeter(grid=[[1, 0]]))

# Problem - https://leetcode.com/problems/island-perimeter/description/
