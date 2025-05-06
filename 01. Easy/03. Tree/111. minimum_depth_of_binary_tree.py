from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if not root.left and not root.right:  # Leaf node
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


sol = Solution()

tree = build_tree([3, 9, 20, None, None, 15, 7])

print(sol.minDepth(tree))

tree = build_tree([2, None, 3, None, 4, None, 5, None, 6])

print(sol.minDepth(tree))

# Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
