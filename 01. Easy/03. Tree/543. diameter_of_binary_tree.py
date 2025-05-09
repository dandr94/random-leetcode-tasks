from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            current_diameter = left_height + right_height

            max_diameter = max(current_diameter, left_diameter, right_diameter)

            current_height = 1 + max(left_height, right_height)

            return current_height, max_diameter

        return dfs(root)[1]


sol = Solution()

tree = build_tree([1, 2, 3, 4, 5])

print(sol.diameterOfBinaryTree(tree))

tree = build_tree([1, 2])

print(sol.diameterOfBinaryTree(tree))

# Easy
# https://leetcode.com/problems/diameter-of-binary-tree/
