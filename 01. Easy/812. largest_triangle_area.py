import itertools
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0

        for i in range(len(points)):
            x_1, y_1 = points[i]

            for j in range(i + 1, len(points)):
                x_2, y_2 = points[j]

                for k in range(j + 1, len(points)):
                    x_3, y_3 = points[k]

                    curr_area = abs(0.5 * (x_1 * (y_2 - y_3) + x_2 * (y_3 - y_1) + x_3 * (y_1 - y_2)))

                    if area < curr_area:
                        area = curr_area

        return area

        # return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
        #            for i, j, k in itertools.combinations(points, 3))


sol = Solution()

print(sol.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))  # 2.0
print(sol.largestTriangleArea([[1, 0], [0, 0], [0, 1]]))  # 0.5
print(sol.largestTriangleArea([[4, 6], [6, 5], [3, 1]]))  # 5.5


# Problem - https://leetcode.com/problems/largest-triangle-area/