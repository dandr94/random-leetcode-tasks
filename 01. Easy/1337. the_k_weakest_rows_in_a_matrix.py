from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rankings = {}

        for row in range(len(mat)):
            rankings[row] = sum(mat[row])

        res = sorted(rankings.items(), key=lambda x: x[1])[:k]

        return [row[0] for row in res]


sol = Solution()
print(sol.kWeakestRows(mat=
                       [[1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0],
                        [1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1]],
                       k=3))
print(sol.kWeakestRows(mat=
                       [[1, 0, 0, 0],
                        [1, 1, 1, 1],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]],
                       k=2))

# Problem - https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
