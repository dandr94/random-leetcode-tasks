from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


sol = Solution()

tree = build_tree([3, 9, 20, None, None, 15, 7])
print(sol.maxDepth(tree))

tree = build_tree([1, None, 2])
print(sol.maxDepth(tree))

# Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
