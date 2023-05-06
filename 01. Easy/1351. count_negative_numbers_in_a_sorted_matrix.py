from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row) - start

        count = 0

        for row in grid:
            count += binary_search(row)

        return count


sol = Solution()
print(sol.countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(sol.countNegatives(grid=[[3, 2], [1, 0]]))

# Problem - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
