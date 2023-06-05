from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0

        seen_rows = set()
        seen_cols = set()

        for _type, idx, val in reversed(queries):
            if not _type:
                if idx not in seen_rows:
                    seen_rows.add(idx)
                    res += val * (n - len(seen_cols))
            else:
                if idx not in seen_cols:
                    seen_cols.add(idx)
                    res += val * (n - len(seen_rows))

        return res


sol = Solution()
print(sol.matrixSumQueries(n=3, queries=[[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]))
print(sol.matrixSumQueries(n=3, queries=[[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]))

# Problem - https://leetcode.com/problems/sum-of-matrix-after-queries/description/
