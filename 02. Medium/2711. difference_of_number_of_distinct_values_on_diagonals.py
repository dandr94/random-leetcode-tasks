from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        res = []

        for row in range(rows):
            res.append([0] * cols)

            for col in range(cols):
                r, c = row + 1, col + 1
                u, d = set(), set()

                while 0 <= r < rows and 0 <= c < cols:
                    d.add(grid[r][c])
                    r += 1
                    c += 1

                r, c = row - 1, col - 1

                while 0 <= r < rows and 0 <= c < cols:
                    u.add(grid[r][c])
                    r -= 1
                    c -= 1

                res[row][col] = abs(len(u) - len(d))

        return res



sol = Solution()
print(sol.differenceOfDistinctValues(grid = [[1,2,3],[3,1,5],[3,2,1]]))
print(sol.differenceOfDistinctValues(grid = [[1]]))


# Problem - https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/description/