from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


sol = Solution()

tree = build_tree([1, 2, 3])

print(sol.sumNumbers(tree))

tree = build_tree([4, 9, 0, 5, 1])

print(sol.sumNumbers(tree))

# Medium
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
