from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows == 1:
            return res

        for i in range(1, numRows):
            row = [0 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = res[-1][j - 1] + res[-1][j]

            res.append(row)

        return res


sol = Solution()
print(sol.generate(numRows=5))
print(sol.generate(numRows=1))

# Problem - https://leetcode.com/problems/pascals-triangle/description/
