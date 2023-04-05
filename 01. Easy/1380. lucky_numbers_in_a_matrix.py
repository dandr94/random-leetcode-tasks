from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_list = []
        for row in matrix:
            min_list.append(min(row))

        for col in zip(*matrix):
            max_num = max(col)
            if max_num in min_list:
                return [max_num]


sol = Solution()
print(sol.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(sol.luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(sol.luckyNumbers(matrix=[[7, 8], [1, 2]]))

# Problem - https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
