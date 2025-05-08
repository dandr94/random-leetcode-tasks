from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0

            if not node.left and not node.right and is_left:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


sol = Solution()

tree = build_tree([3, 9, 20, None, None, 15, 7])

print(sol.sumOfLeftLeaves(tree))

tree = build_tree([1])

print(sol.sumOfLeftLeaves(tree))

# Easy
# https://leetcode.com/problems/sum-of-left-leaves/
