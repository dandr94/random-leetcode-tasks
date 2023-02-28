from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for (x, y) in coordinates[2:]:
            if (y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1):
                return False
        return True


sol = Solution()
print(sol.checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(sol.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))

# Problem - https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
