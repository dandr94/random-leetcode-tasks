from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0

            left_height = check_balance(node.left)

            if left_height == -1:
                return -1

            right_height = check_balance(node.right)

            if right_height == -1:
                return -1

            height_diff = abs(left_height - right_height)

            if height_diff > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check_balance(root) != -1


sol = Solution()

tree = build_tree([3, 9, 20, None, None, 15, 7])

print(sol.isBalanced(tree))

tree = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])

print(sol.isBalanced(tree))

tree = build_tree([])

print(sol.isBalanced(tree))

# Easy
# https://leetcode.com/problems/balanced-binary-tree/description/
