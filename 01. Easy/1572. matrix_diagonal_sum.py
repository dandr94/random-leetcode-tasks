from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()

        _sum = 0
        for idx, num in enumerate(mat):
            _sum += mat[idx][idx]
            visited.add((idx, idx))

            if (idx, len(num) - idx - 1) not in visited:
                _sum += mat[idx][-1 - idx]

        return _sum


sol = Solution()
print(sol.diagonalSum(mat=[[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]))
print(sol.diagonalSum(mat=[[1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1]]))
print(sol.diagonalSum(mat=[[5]]))

# Problem - https://leetcode.com/problems/matrix-diagonal-sum/description/
