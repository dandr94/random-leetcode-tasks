from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        orig_c = image[sr][sc]

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if image[i][j] == color or image[i][j] != orig_c:
                return
            image[i][j] = color
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image


sol = Solution()
print(sol.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
print(sol.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))

# Problem - https://leetcode.com/problems/flood-fill/description/
