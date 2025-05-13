from collections import deque
from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_data = ()
        y_data = ()

        queue = deque()
        queue.append((root, None, 0))  # node, parent, depth

        while queue:
            node, parent, depth = queue.popleft()

            if node.val == x:
                x_data = (parent, depth)

            if node.val == y:
                y_data = (parent, depth)

            if x_data and y_data:
                break

            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        return x_data[0] != y_data[0] and x_data[1] == y_data[1]


sol = Solution()

tree = build_tree([1, 2, 3, 4])

print(sol.isCousins(tree, x=4, y=3))

tree = build_tree([1, 2, 3, None, 4, None, 5])

print(sol.isCousins(tree, x=5, y=4))

tree = build_tree([1, 2, 3, None, 4])

print(sol.isCousins(tree, x=2, y=3))

# Easy
# https://leetcode.com/problems/cousins-in-binary-tree/description/
