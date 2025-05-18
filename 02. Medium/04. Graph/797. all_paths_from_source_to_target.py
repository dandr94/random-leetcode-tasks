from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                res.append(list(path))
                return

            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])

        dfs(0, [0])

        return res


sol = Solution()

print(sol.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))

print(sol.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))

# Medium
# https://leetcode.com/problems/all-paths-from-source-to-target/
