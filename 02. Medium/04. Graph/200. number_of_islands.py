from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def dfs(row, col):
            # Check for out-of-bounds or water or already visited cell
            if (
                    row < 0 or row >= num_rows or
                    col < 0 or col >= num_cols or
                    grid[row][col] == '0' or
                    (row, col) in visited
            ):
                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    island_count += 1

        return island_count


sol = Solution()

print(sol.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(sol.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

# Medium
# https://leetcode.com/problems/number-of-islands/description/
