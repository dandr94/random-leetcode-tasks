from collections import deque
from typing import Optional, List

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_vals = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level_vals.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(level_vals)

        return res


sol = Solution()

tree = build_tree([3, 9, 20, None, None, 15, 7])

print(sol.levelOrder(tree))

tree = build_tree([1])

print(sol.levelOrder(tree))

tree = build_tree([])

print(sol.levelOrder(tree))

# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/
