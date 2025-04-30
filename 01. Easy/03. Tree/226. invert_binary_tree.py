from typing import Optional

from helper import build_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


sol = Solution()

tree = build_tree([4, 2, 7, 1, 3, 6, 9])
print(tree_to_list(sol.invertTree(tree)))

tree = build_tree([2, 1, 3])
print(tree_to_list(sol.invertTree(tree)))

# Easy
# https://leetcode.com/problems/invert-binary-tree/description/
