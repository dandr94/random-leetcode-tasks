from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        visited.add(source)
        queue = deque([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

        return False

        # def dfs(node):
        #     if node == destination:
        #         return True
        #
        #     visited.add(node)
        #
        #     for next_node in graph[node]:
        #         if next_node not in visited:
        #             if dfs(next_node):
        #                 return True
        #
        #     return False
        #
        # return dfs(source)


sol = Solution()

print(sol.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))

print(sol.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

# Easy
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
