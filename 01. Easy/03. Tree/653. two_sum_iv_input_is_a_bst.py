from typing import Optional

from helper import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)


sol = Solution()

tree = build_tree([5, 3, 6, 2, 4, None, 7])

print(sol.findTarget(tree, k=9))

tree = build_tree([5, 3, 6, 2, 4, None, 7])

print(sol.findTarget(tree, k=28))

# Easy
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
